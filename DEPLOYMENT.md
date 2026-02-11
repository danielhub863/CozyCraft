# Streamlit Deployment Guide

## 🚀 Deploy to Streamlit Cloud (Free & Live)

Streamlit Cloud allows you to deploy your app directly from GitHub with automatic updates!

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Add CozyCraft Streamlit app"
git branch -M main

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/CozyCraft.git
git push -u origin main
```

### Step 2: Create Streamlit Cloud Account

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Authorize Streamlit to access your GitHub repositories

### Step 3: Deploy Your App

1. Click "New app" on Streamlit Cloud dashboard
2. Select your repository: `CozyCraft`
3. Select branch: `main`
4. Set main file path: `streamlit_app.py`
5. Click "Deploy!"

Your app will be live in ~1 minute! 🎉

### Step 4: Add Your API Keys (IMPORTANT!)

Your app is now live, but it needs your API keys to function:

1. In Streamlit Cloud dashboard, click on your app's menu (⋮)
2. Click "Settings"
3. Click "Secrets" tab
4. Add the following and click "Save":

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
HUGGINGFACE_API_KEY = "your_huggingface_token_here"
```

### Step 5: Update App to Use Secrets

Your app will now read from Streamlit's secrets management! ✅

---

## 📝 Running Locally First (Optional)

Test before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Create local secrets file
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit with your API keys
nano .streamlit/secrets.toml

# Run the app
streamlit run streamlit_app.py
```

Your app will be at `http://localhost:8501`

---

## 🔑 Getting Your API Keys

### Google Gemini (Free)
1. Visit [aistudio.google.com](https://aistudio.google.com)
2. Click "Get API Key"
3. Click "Create API key in new project"
4. Copy your API key

### Replicate (Free with Credits)
1. Visit [replicate.com](https://replicate.com)
2. Sign up (free account, includes free credits)
3. Go to Account → API Tokens
4. Copy your API token
5. Add to Streamlit Secrets as `REPLICATE_API_KEY`

**Note:** Replicate replaced Hugging Face for more reliable image generation!

---

## 🔄 Automatic Updates

Once deployed to Streamlit Cloud:
- Every push to `main` branch automatically updates your app
- No need to redeploy manually
- Changes live within seconds!

### Push updates:
```bash
git add .
git commit -m "Update app"
git push
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError"
- Streamlit Cloud may need time to install dependencies
- Check the "Manage app" → "Reboot app" option

### "API Key not found"
- Make sure you added secrets in Streamlit Cloud dashboard
- Secrets are different from environment variables
- Use `st.secrets["GEMINI_API_KEY"]` in code (already configured)

### "Image generation failed"
- Rate limited (free tier limit)
- Wait a moment and try again
- Check Hugging Face token is valid

### App takes too long to load
- Streamlit Cloud free tier has limited resources
- It's normal to wait ~30 seconds on first load

---

## 📊 Public Sharing

Your Streamlit app is public by default!

Share your app URL: `https://share.streamlit.io/YOUR_USERNAME/CozyCraft`

---

## 🔐 Security Notes

- **Never** commit API keys to GitHub
- Use Streamlit Secrets (already configured)
- Secrets are encrypted and not visible in logs
- Each deployment can have different secrets

---

## 💡 Next Steps

After deployment, consider:
- [ ] Add custom domain (Streamlit premium)
- [ ] Add user authentication
- [ ] Add design history/favorites
- [ ] Integrate payment processing
- [ ] Add email notifications

---

Happy deploying! 🚀
