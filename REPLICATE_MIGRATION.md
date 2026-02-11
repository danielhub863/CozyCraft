# 🎨 Migration from Hugging Face to Replicate

## What Changed?

Your CozyCraft app has been migrated from **Hugging Face** to **Replicate.com** for image generation. This addresses the reliability issues you were experiencing.

## Why Replicate?

- ✅ **More Reliable**: Replicate models are consistently available
- ✅ **Better Image Quality**: Uses Stable Diffusion 3 & FLUX models
- ✅ **Faster Generation**: Optimized infrastructure for image generation
- ✅ **Free Tier**: Includes free credits for all new accounts
- ✅ **No Cold Starts**: No annoying timeouts or "model loading" delays

## Files Updated

### Backend (Node.js Server)
- **`server/services/imageGenerator.js`** - Switched from Hugging Face API to Replicate API
- **`server/package.json`** - Added `replicate` npm package dependency

### Frontend (Streamlit App)
- **`streamlit_app.py`** - Updated to request Replicate token instead of HF token
  - Changed API key input fields
  - Updated image generation logic with Replicate polling
  - Updated error messages and troubleshooting guides

### Documentation
- **`DEPLOYMENT.md`** - Updated API key setup instructions
- **`SECRETS_FORMAT_GUIDE.md`** - Updated secret format examples
- **`REPLICATE_MIGRATION.md`** - This file!

## API Key Changes

### Old (Hugging Face)
```toml
GEMINI_API_KEY = "your_gemini_key"
HUGGINGFACE_API_KEY = "your_hf_token"
```

### New (Replicate)
```toml
GEMINI_API_KEY = "your_gemini_key"
REPLICATE_API_KEY = "your_replicate_token"
```

## How to Update Your Secrets

### If deployed on Streamlit Cloud:
1. Go to your app's **Settings** (menu ⋮)
2. Click **"Secrets"** tab
3. Replace `HUGGINGFACE_API_KEY` with `REPLICATE_API_KEY`
4. Get your Replicate token at: https://replicate.com/account/api-tokens
5. Click **"Save"**
6. Refresh your app

### If running locally:
1. Update your `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "Your Gemini API Key"
REPLICATE_API_KEY = "Your Replicate Token"
```

2. Run the server dependencies install:
```bash
cd server
npm install
```

## Getting Your Replicate API Token

1. Visit **[replicate.com](https://replicate.com)**
2. Sign up (free, no credit card needed)
3. Go to **Account** → **API Tokens**
4. Copy your API token
5. Add it to your Streamlit Secrets as `REPLICATE_API_KEY`

## Image Generation Flow

### Old Flow (Hugging Face)
```
Prompt → HF API → Network Error → Timeout → Failure ❌
```

### New Flow (Replicate)
```
Prompt → Replicate API → Create Prediction → Poll Status → Download Image ✅
```

## What You'll Notice

✅ **Better reliability** - Image generation works consistently
✅ **Faster feedback** - Progress updates during generation
✅ **Better error messages** - Clear troubleshooting guidance
✅ **Fallback option** - Alternative FLUX model available

## Troubleshooting

### "Invalid Replicate API Token"
- Make sure you copied the full token from https://replicate.com/account/api-tokens
- No extra spaces at start/end
- Check Streamlit Secrets are saved

### "No credits available"
- Free accounts start with free credits
- Check your account at https://replicate.com/account/api-tokens
- You can add a payment method for more credits if needed

### Still seeing Hugging Face references?
- Refresh your browser
- Clear browser cache (Cmd/Ctrl + Shift + R)
- Restart your Streamlit app

## Server Setup

If you're running the Node.js server locally, make sure to:

```bash
cd server
npm install  # Installs replicate package
```

Set environment variable:
```bash
export REPLICATE_API_KEY="your_token_here"
node index.js
```

## Support

- Replicate docs: https://replicate.com/docs
- Replicate status: https://status.replicate.com
- Community: https://discord.gg/replicate

---

**Questions?** Check the troubleshooting section in [DEPLOYMENT.md](DEPLOYMENT.md) or [SECRETS_FORMAT_GUIDE.md](SECRETS_FORMAT_GUIDE.md)!
