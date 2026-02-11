# 🎨 CozyCraft - AI Custom Clothing Designer

A full-stack web application that uses AI to design custom clothing based on user measurements. Users input their measurements, clothing preferences, and style, and the app generates a detailed AI prompt, which is then used to generate a photorealistic image of their custom clothing design.

## ✨ Features

- **User-Friendly Measurement Input**: Simple form for entering clothing measurements
- **AI Prompt Generation**: Uses Google Gemini Flash API to create detailed clothing design prompts
- **AI Image Generation**: Creates photorealistic images using Hugging Face Inference API
- **Real-Time Preview**: View generated designs instantly
- **Download & Purchase**: Download generated images or proceed to purchase
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Free Services**: Uses free APIs (Gemini Flash, Hugging Face)

## 🛠️ Tech Stack

- **Streamlit**: Full-stack Python web framework
- **Google Gemini Flash 1.5**: Free AI model for prompt generation
- **Hugging Face Inference API**: Free image generation with Stable Diffusion models
- **Python 3.9+**: Backend language
- **Pillow**: Image processing

### Deployment
- **Streamlit Cloud**: Free hosting directly from GitHub
- Zero-config deployment
- Automatic updates on every push

## 📋 Prerequisites

- Python 3.9 or higher
- GitHub account (for Streamlit Cloud deployment)
- A free Google API key for Gemini
- A free Hugging Face API token

## 🚀 Getting Started

### Deploy Live in 5 Minutes

The easiest way to get your app live:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Add CozyCraft Streamlit app"
   git remote add origin https://github.com/YOUR_USERNAME/CozyCraft.git
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and `streamlit_app.py`
   - Click "Deploy"

3. **Add Your API Keys**
   - In Streamlit Cloud dashboard, click app settings
   - Go to "Secrets" tab
   - Add:
   ```toml
   GEMINI_API_KEY = "your_key"
   HUGGINGFACE_API_KEY = "your_token"
   ```
   - Click "Save"

**Your app is now live!** 🎉

---

### Or Run Locally First

```bash
# Install dependencies
pip install -r requirements.txt

# Create secrets file
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit with your API keys: nano .streamlit/secrets.toml

# Run the app
streamlit run streamlit_app.py
```

App opens at `http://localhost:8501`

---

### Get Your API Keys (2 minutes)

**Google Gemini API:**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click "Get API Key"
3. Click "Create API key in new project"
4. Copy the key

**Hugging Face API Token:**
1. Go to [huggingface.co](https://huggingface.co)
2. Sign up or log in
3. Settings → Access Tokens
4. Create "Read" token
5. Copy the token

No credit card required! 🎉

## 📖 How It Works

1. **User Input**: Fill in measurements, clothing type, style, and preferences in the web form
2. **Prompt Generation**: Streamlit sends data to Google Gemini Flash API to generate a detailed fashion design prompt
3. **Image Generation**: The prompt is sent to Hugging Face Inference API which generates a photorealistic image
4. **Display**: The generated image is displayed instantly in your browser
5. **Download**: Download the image or proceed to checkout (if connected to payment system)

## 🎨 Features

### Measurement Form
- Clothing type selection (T-Shirt, Dress, Jacket, etc.)
- Style selection (Casual, Formal, Vintage, etc.)
- Precise measurements (chest, waist, length, sleeves)
- Material and color options
- Custom design preferences
- Fit selection (Slim, Regular, Relaxed, Oversized)

### Generated Design
- AI-generated photorealistic clothing images
- View the AI prompt used for generation
- Download generated images as PNG
- Purchase integration ready

### Deployment
- One-click deployment to Streamlit Cloud
- Automatic updates on GitHub push
- No server maintenance needed
- Built-in secret management for API keys

## 🔧 Configuration

### Using Streamlit Cloud (Recommended)

Add secrets directly in Streamlit Cloud dashboard:

1. Go to your app's settings
2. Click "Secrets" tab
3. Add these variables:
   ```toml
   GEMINI_API_KEY = "your_google_gemini_api_key"
   HUGGINGFACE_API_KEY = "your_huggingface_api_token"
   ```
4. Click "Save"

### Using Locally

Create `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_google_gemini_api_key"
HUGGINGFACE_API_KEY = "your_huggingface_api_token"
```

⚠️ **Never commit this file to GitHub!** (Already in .gitignore)

## 📦 Project Structure

```
CozyCraft/
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .streamlit/
│   ├── config.toml           # Streamlit configuration
│   └── secrets.toml.example  # Example secrets file (use for local dev)
├── DEPLOYMENT.md             # Deployment guide
├── README.md                 # This file
└── .gitignore
```

**That's it!** One file to deploy.

## 🐛 Troubleshooting

### "API Key not found" Error
- **Local**: Ensure `.streamlit/secrets.toml` exists with your keys
- **Streamlit Cloud**: Check that secrets are added in dashboard (Settings → Secrets)
- Restart the app after adding secrets

### "Image generation failed"
- Hugging Face free tier has rate limits
- Wait a moment and try again
- Ensure your Hugging Face token is valid and has "Read" permission

### "ModuleNotFoundError"
- **Streamlit Cloud**: Click "Reboot app" in app settings
- **Local**: Run `pip install -r requirements.txt` again

### Slow image generation
- First generation takes 1-2 minutes (normal on free tier)
- Streamlit Cloud free tier has limited resources
- Back-to-back requests may queue

### "Connection refused" locally
- Make sure you ran `streamlit run streamlit_app.py`
- Check port 8501 is not in use

### CORS or connection errors
- Not applicable with Streamlit (single Python app)
- If deploying your own Streamlit server, ensure correct port

## 💡 Extending the Application

### Add Database (Store Designs)
```bash
pip install streamlit-option-menu firebase-admin
```
Then add user designs database integration.

### Add User Accounts
```bash
pip install streamlit-authenticator
```

### Add Payment Integration
```bash
pip install stripe
```
Integrate Stripe for checkout.

### Improve Image Generation
- Try other Hugging Face models
- Use Replicate API for more options
- Add model selection UI

### Add Email Notifications
```bash
pip install python-dotenv smtplib
```

### Deploy to Custom Domain
- Upgrade to Streamlit+
- Use nginx or custom server

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Google Gemini API](https://ai.google.dev)
- [Hugging Face Inference API](https://huggingface.co/docs/api-inference)
- [Streamlit Cloud Deployment](https://docs.streamlit.io/streamlit-cloud/get-started)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions, please open an issue in the repository.

---

**Happy Designing! 🎨✨** 
