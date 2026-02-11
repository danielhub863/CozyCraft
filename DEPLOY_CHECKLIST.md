# ⚡ CozyCraft - Deploy Checklist (5 min)

Use this checklist to deploy your app live in 5 minutes!

---

## ☑️ Pre-Deployment (Get API Keys - 4 min)

- [ ] **Google Gemini API Key**
  - [ ] Visit: https://aistudio.google.com  
  - [ ] Click: "Get API Key" 
  - [ ] Click: "Create API key in new project"
  - [ ] Copy your API key
  - [ ] Save it temporarily (you'll need it soon)

- [ ] **Hugging Face API Token**
  - [ ] Visit: https://huggingface.co
  - [ ] Sign up (free)
  - [ ] Go to: Settings → Access Tokens
  - [ ] Click: "New token"
  - [ ] Select: "Read" permission
  - [ ] Copy your token
  - [ ] Save it temporarily

---

## ☑️ GitHub Push (1 min)

```bash
cd /workspaces/CozyCraft
git init
git add .
git commit -m "Add CozyCraft"
git remote add origin https://github.com/YOUR_USERNAME/CozyCraft.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

---

## ☑️ Deploy to Streamlit Cloud (Automated - <1 min)

1. [ ] Go to: https://share.streamlit.io
2. [ ] Sign in (use your GitHub account)
3. [ ] Click: "New app"
4. [ ] Select:
   - Repository: `YOUR_USERNAME/CozyCraft`
   - Branch: `main`
   - File: `streamlit_app.py`
5. [ ] Click: "Deploy"
6. [ ] Wait 1-2 minutes... (it's deploying!)
7. [ ] Your app URL appears at top! 🎉

---

## ☑️ Add API Keys to Streamlit Cloud (1 min)

1. [ ] Find your app in dashboard
2. [ ] Click menu (⋮) → Settings
3. [ ] Click: "Secrets" tab
4. [ ] Paste this and **replace YOUR KEYS**:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
HUGGINGFACE_API_KEY = "YOUR_HUGGINGFACE_TOKEN_HERE"
```

5. [ ] Click: "Save"

**Your app is now LIVE! ✅**

---

## ✨ Test Your App

- [ ] Click your app URL
- [ ] Enter measurements (or use defaults)
- [ ] Click "✨ Generate Design"
- [ ] Wait for image to generate (1-2 min)
- [ ] See your AI-designed clothing! 🎨

---

## 🎉 Success!

Your app is deployed and fully functional!

**Your app URL**: `https://share.streamlit.io/YOUR_USERNAME/CozyCraft`

**Share this URL** with anyone!

---

## 📝 Remember

- Changes push automatically: `git push` → auto-deploys
- API keys go in Streamlit Secrets (not in code)
- Free tier works great (rate limits apply)
- No credit card required for any service!

---

**That's it! You have a production AI app live! 🚀**
