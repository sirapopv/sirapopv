# Quick Deploy Guide - Get Online in 5 Minutes

Choose your deployment method:

## 🚀 Option 1: Railway.app (Easiest - Recommended)

**Time: 5 minutes | Cost: ~$5/month**

1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Railway auto-deploys!
6. Access your app at the provided URL

**Add custom domain:**
- Click project → Settings → Domains
- Add your domain
- Update DNS: `CNAME podcast → your-railway-url`

---

## 🆓 Option 2: Render.com (Free Tier)

**Time: 5 minutes | Cost: Free (or $7/mo for always-on)**

1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. New → Web Service
4. Connect repository
5. Select "Docker" environment
6. Deploy

**Note:** Free tier spins down after 15 min of inactivity

---

## 🖥️ Option 3: VPS (Full Control)

**Time: 30 minutes | Cost: $4-12/month**

### Automated Setup (Ubuntu 22.04+):

```bash
# SSH into your server
ssh root@your-server-ip

# Download and run setup script
curl -sSL https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/deploy_vps.sh | bash
```

Or manually:

```bash
# SSH into server
ssh root@your-server-ip

# Clone repository
git clone <your-repo-url>
cd youtube-video-converter

# Run deployment script
chmod +x deploy_vps.sh
./deploy_vps.sh
```

Follow the prompts to enter your domain and email.

---

## 🐳 Option 4: Any Server with Docker

**Time: 10 minutes**

```bash
# Clone repository
git clone <your-repo-url>
cd youtube-video-converter

# Run with Docker Compose
docker-compose up -d

# Access at http://your-server-ip:8501
```

---

## 🔒 Add Password Protection (Optional)

### Step 1: Generate password hash

```bash
python3 generate_password_hash.py
```

### Step 2: Set environment variables

**For Docker Compose**, add to `docker-compose.yml`:

```yaml
environment:
  - AUTH_USERNAME=admin
  - AUTH_PASSWORD_HASH=your_generated_hash
```

**For Cloud Platforms**, add in dashboard:
- `AUTH_USERNAME` = `admin`
- `AUTH_PASSWORD_HASH` = `your_generated_hash`

### Step 3: Use authenticated app

Update `Dockerfile` last line to:

```dockerfile
CMD ["streamlit", "run", "app_auth.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🌐 Custom Domain Setup

### For Railway/Render:

1. Add DNS record:
   ```
   Type: CNAME
   Name: podcast
   Value: <platform-provided-url>
   ```

### For VPS:

1. Add DNS record:
   ```
   Type: A
   Name: podcast
   Value: <your-server-ip>
   ```

2. SSL is auto-configured by deployment script!

---

## ✅ After Deployment

1. Visit your app URL
2. Configure API key in sidebar (one-time)
3. Add style instructions (optional)
4. Upload sample script (optional)
5. Start converting videos!

---

## 📊 Platform Comparison

| Platform | Setup | Cost | Best For |
|----------|-------|------|----------|
| Railway | ⭐ Easiest | $5/mo | Quick start |
| Render | ⭐ Easy | Free* | Testing |
| VPS | ⭐⭐⭐ Medium | $4-12/mo | Production |

*Free tier has limitations (spins down when idle)

---

## 🆘 Need Help?

See full deployment guide: [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🎉 That's It!

Your YouTube to Podcast Converter is now accessible from anywhere on the internet!
