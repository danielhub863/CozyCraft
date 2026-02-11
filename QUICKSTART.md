# 🎨 CozyCraft - Quick Start Guide

## ⚡ Deploy Live in 3 Steps (5 minutes)

### Step 1: Get Your API Keys (2 min)

**Google Gemini:**
1. Go to https://aistudio.google.com
2. Click "Get API Key" → "Create API key in new project"
3. Copy the key

**Hugging Face:**
1. Go to https://huggingface.co → Sign up (free)
2. Settings → Access Tokens → New Token
3. Select "Read" permission
4. Copy the token

### Step 2: Push to GitHub (2 min)

```bash
cd /workspaces/CozyCraft

# First time setup
git init
git add .
git commit -m "Add CozyCraft Streamlit app"
git remote add origin https://github.com/YOUR_USERNAME/CozyCraft.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Streamlit Cloud (1 min)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your `CozyCraft` repository
5. Set main file: `streamlit_app.py`
6. Click "Deploy"

**Your app is live!** 🎉

### Step 4: Add Your API Keys

1. In Streamlit Cloud dashboard, find your app
2. Click menu (⋮) → Settings
3. Click "Secrets" tab
4. Paste this (replace with YOUR keys):
```toml
GEMINI_API_KEY = "paste_your_gemini_key_here"
HUGGINGFACE_API_KEY = "paste_your_huggingface_token_here"
```
5. Click "Save"

**Done!** Your app now has full access to AI APIs ✅

---

## 🏃 Run Locally First (Optional)

Test before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Create local secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit secrets with YOUR keys
nano .streamlit/secrets.toml

# Run the app
streamlit run streamlit_app.py
```

App opens at http://localhost:8501

---

## 🔑 Your API Keys

### Where to get them:
- **Gemini**: [https://aistudio.google.com](https://aistudio.google.com)
- **Hugging Face**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### Security:
- Never put API keys in code
- Use Streamlit Secrets (already configured)
- Free tier works great! No credit card needed

---

## 📝 What Next?

1. Test the app at your Streamlit URL
2. Fill in measurements and generate a design
3. Share your app URL with others
4. Push updates: `git push` (auto-deploys!)

---

## 🐛 Stuck?

- **"API Key not found"** → Check Streamlit Cloud Secrets tab
- **"Module not found"** → Reboot app in Streamlit Cloud settings
- **"Rate limited"** → Wait 30 seconds, try again

Full help in [DEPLOYMENT.md](DEPLOYMENT.md) and [README.md](README.md)

---

## ✨ Share Your App

Once live, share this link:
```
https://share.streamlit.io/YOUR_USERNAME/CozyCraft
```

That's it! You have a production AI app running! 🚀

