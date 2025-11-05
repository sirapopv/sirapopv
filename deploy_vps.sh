#!/bin/bash
# VPS Deployment Script for YouTube to Podcast Converter
# Run this script on a fresh Ubuntu 22.04+ server

set -e  # Exit on error

echo "=========================================="
echo "YouTube to Podcast Converter - VPS Setup"
echo "=========================================="
echo ""

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "⚠️  This script should be run as root or with sudo"
   echo "Usage: sudo bash deploy_vps.sh"
   exit 1
fi

# Get user input
echo "Please provide the following information:"
echo ""
read -p "Your domain name (e.g., podcast.example.com): " DOMAIN
read -p "Your email for SSL certificate: " EMAIL

if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then
    echo "❌ Domain and email are required!"
    exit 1
fi

echo ""
echo "=========================================="
echo "Starting deployment..."
echo "=========================================="
echo ""

# Update system
echo "📦 Updating system packages..."
apt update && apt upgrade -y

# Install Docker
echo "🐳 Installing Docker..."
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
else
    echo "✅ Docker already installed"
fi

# Install Docker Compose
echo "🐳 Installing Docker Compose..."
if ! command -v docker-compose &> /dev/null; then
    apt install docker-compose -y
else
    echo "✅ Docker Compose already installed"
fi

# Install Nginx
echo "🌐 Installing Nginx..."
if ! command -v nginx &> /dev/null; then
    apt install nginx -y
else
    echo "✅ Nginx already installed"
fi

# Install Certbot
echo "🔒 Installing Certbot..."
if ! command -v certbot &> /dev/null; then
    apt install certbot python3-certbot-nginx -y
else
    echo "✅ Certbot already installed"
fi

# Clone repository (you might want to change this)
echo "📥 Setting up application..."
cd /opt
if [ -d "youtube-converter" ]; then
    echo "⚠️  Directory already exists, pulling latest changes..."
    cd youtube-converter
    git pull
else
    echo "Enter your repository URL (or press Enter to skip clone):"
    read REPO_URL
    if [ ! -z "$REPO_URL" ]; then
        git clone $REPO_URL youtube-converter
        cd youtube-converter
    else
        echo "❌ Skipping git clone. Please manually copy files to /opt/youtube-converter"
        exit 1
    fi
fi

# Create necessary directories
mkdir -p output settings

# Start Docker containers
echo "🚀 Starting application..."
docker-compose up -d

# Wait for container to be ready
echo "⏳ Waiting for application to start..."
sleep 10

# Configure Nginx
echo "🌐 Configuring Nginx..."
cat > /etc/nginx/sites-available/youtube-converter << EOF
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
        proxy_buffering off;
    }

    client_max_body_size 100M;
}
EOF

# Enable site
ln -sf /etc/nginx/sites-available/youtube-converter /etc/nginx/sites-enabled/

# Test Nginx configuration
echo "🧪 Testing Nginx configuration..."
nginx -t

# Restart Nginx
echo "🔄 Restarting Nginx..."
systemctl restart nginx

# Setup SSL with Certbot
echo "🔒 Setting up SSL certificate..."
certbot --nginx -d $DOMAIN --non-interactive --agree-tos --email $EMAIL --redirect

# Configure firewall
echo "🔥 Configuring firewall..."
if command -v ufw &> /dev/null; then
    ufw allow 22/tcp
    ufw allow 80/tcp
    ufw allow 443/tcp
    ufw --force enable
    echo "✅ Firewall configured"
else
    echo "⚠️  UFW not found, please configure firewall manually"
fi

echo ""
echo "=========================================="
echo "✅ Deployment Complete!"
echo "=========================================="
echo ""
echo "Your app is now live at: https://$DOMAIN"
echo ""
echo "Next steps:"
echo "1. Visit your domain and configure API key in the web interface"
echo "2. Check logs: docker-compose logs -f"
echo "3. Monitor resources: docker stats"
echo ""
echo "Useful commands:"
echo "  - View logs: cd /opt/youtube-converter && docker-compose logs -f"
echo "  - Restart app: cd /opt/youtube-converter && docker-compose restart"
echo "  - Update app: cd /opt/youtube-converter && git pull && docker-compose up -d --build"
echo "  - Backup settings: tar -czf backup-settings.tar.gz settings/"
echo ""
echo "SSL certificate will auto-renew. Test renewal with:"
echo "  certbot renew --dry-run"
echo ""
echo "=========================================="
