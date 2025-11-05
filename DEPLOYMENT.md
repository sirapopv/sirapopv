# Deployment Guide - YouTube to Podcast Converter

This guide explains how to deploy the YouTube to Podcast Converter on your website/server.

## 📋 Table of Contents

1. [Quick Deploy Options](#quick-deploy-options)
2. [Docker Deployment (Recommended)](#docker-deployment)
3. [Cloud Platform Deployment](#cloud-platform-deployment)
   - [Railway.app (Easiest)](#1-railwayapp-easiest)
   - [Render.com (Free Tier)](#2-rendercom-free-tier)
   - [DigitalOcean](#3-digitalocean)
   - [AWS / Google Cloud](#4-aws--google-cloud)
4. [VPS Deployment](#vps-deployment)
5. [Security & Authentication](#security--authentication)
6. [Custom Domain Setup](#custom-domain-setup)
7. [Troubleshooting](#troubleshooting)

---

## Quick Deploy Options

### Comparison Table

| Platform | Difficulty | Cost | Best For |
|----------|-----------|------|----------|
| Railway.app | ⭐ Easy | ~$5/mo | Quick start |
| Render.com | ⭐⭐ Easy | Free tier | Testing |
| DigitalOcean | ⭐⭐⭐ Medium | $4-12/mo | Production |
| VPS (any) | ⭐⭐⭐⭐ Medium | $5-20/mo | Full control |
| AWS/GCP | ⭐⭐⭐⭐⭐ Hard | Variable | Enterprise |

---

## Docker Deployment

### Prerequisites

- Docker installed
- Docker Compose installed (optional but recommended)

### Option 1: Using Docker Compose (Recommended)

```bash
# Clone your repository
git clone <your-repo-url>
cd youtube-video-converter

# Build and run with Docker Compose
docker-compose up -d

# Access at: http://localhost:8501
```

### Option 2: Using Docker directly

```bash
# Build the image
docker build -t youtube-converter .

# Run the container
docker run -d \
  -p 8501:8501 \
  -v $(pwd)/output:/app/output \
  -v $(pwd)/settings:/app/settings \
  --name youtube-converter \
  youtube-converter

# Access at: http://localhost:8501
```

### Docker Commands

```bash
# View logs
docker logs youtube-converter

# Stop container
docker stop youtube-converter

# Start container
docker start youtube-converter

# Remove container
docker rm -f youtube-converter

# Rebuild after code changes
docker-compose down
docker-compose up -d --build
```

---

## Cloud Platform Deployment

### 1. Railway.app (Easiest)

**Cost:** ~$5/month (pay as you go)
**Time:** 5 minutes

#### Steps:

1. **Go to [Railway.app](https://railway.app)**

2. **Sign up** with GitHub

3. **Create New Project** → **Deploy from GitHub repo**

4. **Select your repository**

5. **Add Environment Variables** (in Railway dashboard):
   ```
   PORT=8501
   ```

6. **Railway auto-detects Dockerfile** and deploys!

7. **Access your app** at the provided Railway URL

#### Add Custom Domain:

1. Go to project settings
2. Click "Domains"
3. Add your domain (e.g., `podcast.yourdomain.com`)
4. Update DNS:
   ```
   Type: CNAME
   Name: podcast
   Value: <your-railway-url>
   ```

---

### 2. Render.com (Free Tier)

**Cost:** Free (with limitations) or $7/month
**Time:** 10 minutes

#### Steps:

1. **Go to [Render.com](https://render.com)**

2. **Sign up** with GitHub

3. **New** → **Web Service**

4. **Connect repository**

5. **Configure:**
   ```
   Name: youtube-converter
   Environment: Docker
   Region: Choose closest to you
   Branch: main
   Plan: Free (or Starter for better performance)
   ```

6. **Add Environment Variables:**
   ```
   PORT=8501
   STREAMLIT_SERVER_PORT=8501
   ```

7. **Deploy**

8. **Access at:** `https://your-app-name.onrender.com`

#### Note on Free Tier:

- Spins down after 15 min inactivity
- First request takes ~30 seconds to wake up
- Upgrade to Starter ($7/mo) for always-on

---

### 3. DigitalOcean

**Cost:** $4-12/month (Droplet)
**Time:** 30 minutes

#### Option A: Using App Platform (Easier)

1. **Go to [DigitalOcean](https://digitalocean.com)**

2. **Create** → **Apps**

3. **Connect GitHub** → Select repository

4. **Detected:** Dockerfile

5. **Configure:**
   ```
   HTTP Port: 8501
   Plan: Basic ($5/mo recommended)
   ```

6. **Deploy**

#### Option B: Using Droplet (More Control)

See [VPS Deployment](#vps-deployment) section below.

---

### 4. AWS / Google Cloud

**For Enterprise Deployments**

#### AWS Options:

- **Elastic Beanstalk** (Easiest)
- **ECS with Fargate** (Recommended)
- **EC2** (Full control)

#### GCP Options:

- **Cloud Run** (Easiest, serverless)
- **App Engine**
- **Compute Engine**

**Detailed guides available online for these platforms.**

---

## VPS Deployment

Deploy on any VPS (DigitalOcean, Linode, Vultr, Hetzner, etc.)

### Prerequisites

- Ubuntu 22.04 or newer
- Root or sudo access
- Domain name (optional)

### Step 1: Server Setup

```bash
# SSH into your server
ssh root@your-server-ip

# Update system
apt update && apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
apt install docker-compose -y

# Install nginx (for reverse proxy)
apt install nginx -y
```

### Step 2: Clone and Deploy

```bash
# Clone repository
cd /opt
git clone <your-repo-url> youtube-converter
cd youtube-converter

# Create required directories
mkdir -p output settings

# Build and run
docker-compose up -d

# Verify running
docker ps
```

### Step 3: Setup Nginx Reverse Proxy

```bash
# Create nginx config
nano /etc/nginx/sites-available/youtube-converter
```

**Add this configuration:**

```nginx
server {
    listen 80;
    server_name your-domain.com;  # Change this

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Enable site
ln -s /etc/nginx/sites-available/youtube-converter /etc/nginx/sites-enabled/

# Test configuration
nginx -t

# Restart nginx
systemctl restart nginx
```

### Step 4: Setup SSL with Let's Encrypt

```bash
# Install Certbot
apt install certbot python3-certbot-nginx -y

# Get SSL certificate
certbot --nginx -d your-domain.com

# Auto-renewal is configured automatically
```

**Your app is now live at:** `https://your-domain.com`

### Maintenance Commands

```bash
# View logs
docker-compose logs -f

# Restart app
docker-compose restart

# Update app
cd /opt/youtube-converter
git pull
docker-compose down
docker-compose up -d --build

# Backup settings
tar -czf settings-backup-$(date +%Y%m%d).tar.gz settings/
```

---

## Security & Authentication

### Option 1: Password Protection (Built-in)

Use `app_auth.py` instead of `app.py`:

1. **Generate password hash:**

```python
python3 -c "import hashlib; print(hashlib.sha256('your_password'.encode()).hexdigest())"
```

2. **Set environment variables:**

```bash
# For Docker Compose, add to docker-compose.yml:
environment:
  - AUTH_USERNAME=admin
  - AUTH_PASSWORD_HASH=your_hash_here

# For VPS, export before running:
export AUTH_USERNAME=admin
export AUTH_PASSWORD_HASH=your_hash_here
```

3. **Update Dockerfile to use app_auth.py:**

```dockerfile
CMD ["streamlit", "run", "app_auth.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Option 2: Nginx Basic Auth

```bash
# Install htpasswd
apt install apache2-utils -y

# Create password file
htpasswd -c /etc/nginx/.htpasswd username

# Add to nginx config (before location block):
auth_basic "Restricted Access";
auth_basic_user_file /etc/nginx/.htpasswd;
```

### Option 3: Cloudflare Access

For more advanced authentication with SSO:

1. Add site to Cloudflare
2. Enable Cloudflare Access
3. Configure authentication rules

---

## Custom Domain Setup

### 1. Point Domain to Your Server

#### For Cloud Platforms (Railway, Render):

Add DNS record:
```
Type: CNAME
Name: podcast (or @)
Value: <platform-provided-url>
```

#### For VPS:

Add DNS record:
```
Type: A
Name: podcast (or @)
Value: <your-server-ip>
```

### 2. Wait for DNS Propagation

Check with: `dig your-domain.com`

Usually takes 5 minutes to 48 hours.

---

## Environment Variables

For production deployment, you can configure:

```bash
# Streamlit settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true

# Authentication (optional)
AUTH_USERNAME=admin
AUTH_PASSWORD_HASH=<sha256_hash>

# Other settings
OUTPUT_DIR=/app/output
SETTINGS_DIR=/app/settings
```

---

## Monitoring & Logs

### View Application Logs

**Docker:**
```bash
docker logs youtube-converter -f
```

**Docker Compose:**
```bash
docker-compose logs -f
```

### Resource Monitoring

```bash
# Check CPU/memory usage
docker stats youtube-converter

# Check disk usage
df -h
du -sh output/
```

---

## Backup & Restore

### Backup

```bash
# Backup settings (includes API keys, preferences)
tar -czf backup-settings.tar.gz settings/

# Backup output (generated videos)
tar -czf backup-output.tar.gz output/

# Download backups
scp root@your-server:/opt/youtube-converter/backup-*.tar.gz ./
```

### Restore

```bash
# Upload backups
scp backup-settings.tar.gz root@your-server:/opt/youtube-converter/

# Extract
tar -xzf backup-settings.tar.gz

# Restart app
docker-compose restart
```

---

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8501
lsof -i :8501

# Kill process
kill -9 <PID>
```

### Container Won't Start

```bash
# Check logs
docker logs youtube-converter

# Rebuild
docker-compose down
docker-compose up -d --build
```

### Out of Memory

```bash
# Increase Docker memory limit
docker update --memory="2g" youtube-converter

# Or update docker-compose.yml:
services:
  youtube-converter:
    mem_limit: 2g
```

### ffmpeg Not Found

The Dockerfile includes ffmpeg. If issues persist:

```bash
# Rebuild image
docker-compose build --no-cache
docker-compose up -d
```

### SSL Certificate Issues

```bash
# Renew certificate
certbot renew

# Restart nginx
systemctl restart nginx
```

---

## Performance Optimization

### 1. Increase Resources

For Docker Compose, add to `docker-compose.yml`:

```yaml
services:
  youtube-converter:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
```

### 2. Enable Caching

Configure in `.streamlit/config.toml`:

```toml
[server]
enableStaticServing = true
```

### 3. Add CDN

Use Cloudflare or similar for:
- Static file caching
- DDoS protection
- Faster global access

---

## Cost Estimates

| Setup | Monthly Cost | Best For |
|-------|-------------|----------|
| Railway | $5-15 | Quick start, low traffic |
| Render Free | $0 | Testing only |
| Render Starter | $7 | Small projects |
| DigitalOcean Droplet | $4-12 | Medium traffic |
| VPS (Hetzner) | $4-8 | Best value |
| AWS/GCP | $10-100+ | Enterprise |

**Note:** API costs (Google Gemini) are separate and depend on usage.

---

## Next Steps

After deployment:

1. ✅ Test the application
2. ✅ Set up backups
3. ✅ Configure monitoring
4. ✅ Add custom domain
5. ✅ Enable SSL
6. ✅ Set up authentication (if public)
7. ✅ Configure firewall rules

---

## Support

If you encounter issues:

1. Check logs: `docker-compose logs -f`
2. Verify DNS propagation: `dig your-domain.com`
3. Test locally: `docker-compose up`
4. Check firewall: `ufw status`

---

## Security Checklist

Before going live:

- [ ] Enable authentication (if public)
- [ ] Set up SSL certificate
- [ ] Configure firewall
- [ ] Regular backups
- [ ] Update system packages
- [ ] Monitor disk space
- [ ] Set up log rotation
- [ ] Restrict SSH access
- [ ] Use strong passwords
- [ ] Keep Docker images updated

---

**Your YouTube to Podcast Converter is now live on the web!** 🎉
