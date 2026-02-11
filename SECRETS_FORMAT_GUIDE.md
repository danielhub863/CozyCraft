# 🔑 Streamlit Secrets Format Guide

## Exact Format for Secrets Tab

Your Streamlit Cloud **Settings → Secrets** tab should look **EXACTLY** like this:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
REPLICATE_API_KEY = "your_actual_replicate_token_here"
```

---

## ✅ Correct Examples

### Example 1: Real-looking (don't use these keys!)
```toml
GEMINI_API_KEY = "AIzaSyDx1234567890abcdefghijklmnopqrst"
REPLICATE_API_KEY = "caaeb8e....."
```

### Example 2: Minimal format
```toml
GEMINI_API_KEY = "YOUR_KEY_HERE"
REPLICATE_API_KEY = "YOUR_TOKEN_HERE"
```

---

## ❌ WRONG Formats (Don't Do These!)

### ❌ Wrong 1: Without quotes
```toml
GEMINI_API_KEY = AIzaSyDx1234567890abcdefghijklmnopqrst
REPLICATE_API_KEY = caaeb8e.....
```

### ❌ Wrong 2: Extra spaces around equals
```toml
GEMINI_API_KEY  =  "your_key"
REPLICATE_API_KEY  =  "your_token"
```

### ❌ Wrong 3: Single quotes instead of double quotes
```toml
GEMINI_API_KEY = 'your_key'
REPLICATE_API_KEY = 'your_token'
```

### ❌ Wrong 4: Variables in curly braces
```toml
GEMINI_API_KEY = {your_key}
REPLICATE_API_KEY = {your_token}
```

### ❌ Wrong 5: Comments on same line
```toml
GEMINI_API_KEY = "your_key" # This is my gemini key
```

### ❌ Wrong 6: Missing line breaks
```toml
GEMINI_API_KEY = "your_key" REPLICATE_API_KEY = "your_token"
```

---

## 📋 Step-by-Step: Adding Secrets Correctly

1. **Go to your Streamlit Cloud app**
   - Dashboard → Click your app

2. **Click the menu (⋮)** in top right

3. **Click "Settings"**

4. **Click "Secrets"** tab on left

5. **Clear any existing text** in the box

6. **Paste EXACTLY this** (replacing YOUR KEYS):
   ```toml
   GEMINI_API_KEY = "your_actual_key_from_aistudio_google_com"
   REPLICATE_API_KEY = "your_actual_token_from_replicate_com"
   ```

7. **Click "Save"** button

8. **Refresh your app** (browser refresh)

---

## 🔍 Verify Your Keys

### Check Your Gemini Key Format
- Should be ~39 characters
- Starts with `AIza` 
- Contains numbers and letters
- Example: `AIzaSyDx1234567890abcdefghijklmnopqrst`

### Check Your Replicate Token Format
- Can be various lengths (usually 40+ characters)
- Found at: https://replicate.com/account/api-tokens
- Example looks like: `caaeb8e60c754b42...`

---

## 🆘 If Still Getting "Invalid API Key" Error

Try this checklist:

- [ ] API keys have NO extra spaces before/after
- [ ] Using DOUBLE QUOTES (`"`) not single quotes (`'`)
- [ ] Exactly TWO lines (one line per key)
- [ ] Format is: `KEY_NAME = "value"`
- [ ] Refresh browser after saving
- [ ] Keys are copied from official sources:
  - Gemini: https://aistudio.google.com
  - Replicate: https://replicate.com/account/api-tokens

---

## 📸 Visual Check

The Secrets editor should look like a simple text box with two lines:

```
Line 1: GEMINI_API_KEY = "paste_your_key_here"
Line 2: REPLICATE_API_KEY = "paste_your_token_here"
```

Nothing else, no JSON, no extra formatting!

---

## ✅ After Saving

1. Click **"Save"** button
2. You should see: **"Secrets updated!"** message
3. Refresh the app page in your browser
4. Try generating a design again

If you STILL get an error after this, the issue might be:
- Your Gemini API key doesn't have the right permissions
- Your Gemini key is for a different project than the one you created it in
- Your Replicate account has no available credits (free accounts get free credits to start)

Try getting brand new keys from the official sources and following these steps exactly!
