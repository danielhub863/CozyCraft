import streamlit as st
from google.generativeai import GenerativeModel, configure
import requests
from io import BytesIO
from PIL import Image

# Configure page
st.set_page_config(
    page_title="🎨 CozyCraft - AI Clothing Designer",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        max-width: 1400px;
    }
    .stButton > button {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
    }
    .design-container {
        border-radius: 12px;
        padding: 20px;
        background-color: #f8f9ff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'generated_image' not in st.session_state:
    st.session_state.generated_image = None
if 'generated_prompt' not in st.session_state:
    st.session_state.generated_prompt = None

# Header
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1>🎨 CozyCraft</h1>
        <p style="font-size: 1.2rem; color: #666;">AI-Powered Custom Clothing Designer</p>
        <p style="color: #999;">Design your perfect custom clothing with AI</p>
    </div>
    """, unsafe_allow_html=True)

# API Key Management
with st.sidebar:
    st.header("⚙️ Configuration")
    
    st.write("**If deployed on Streamlit Cloud:**")
    st.caption("✅ API keys come from Settings → Secrets")
    
    st.divider()
    
    # Try to get keys from Streamlit secrets first
    try:
        gemini_key = st.secrets["GEMINI_API_KEY"]
        hf_key = st.secrets["HUGGINGFACE_API_KEY"]
        st.success("✅ API Keys loaded from Streamlit Secrets")
    except (KeyError, FileNotFoundError):
        st.info("📝 Using manual API key input (local development)")
        
        gemini_key = st.text_input(
            "Google Gemini API Key",
            type="password",
            help="Get from: https://aistudio.google.com"
        )
        
        hf_key = st.text_input(
            "Hugging Face API Token",
            type="password",
            help="Get from: https://huggingface.co/settings/tokens"
        )

# Main app
if gemini_key and hf_key:
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("📐 Your Measurements")
        
        # Clothing type and style
        col_type, col_style = st.columns(2)
        with col_type:
            clothing_type = st.selectbox(
                "Clothing Type *",
                ["T-Shirt", "Button-Up Shirt", "Sweater", "Hoodie", "Dress", 
                 "Pants", "Shorts", "Jacket", "Coat", "Skirt"],
                key="clothing_type"
            )
        
        with col_style:
            style = st.selectbox(
                "Style",
                ["Casual", "Formal", "Athletic", "Vintage", "Modern", 
                 "Bohemian", "Minimalist", "Streetwear", "Elegant"],
                key="style"
            )
        
        # Measurements
        st.write("**Enter measurements in inches:**")
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        
        with col_m1:
            chest = st.number_input("Chest", min_value=20.0, max_value=60.0, value=38.0, step=0.5)
        
        with col_m2:
            waist = st.number_input("Waist", min_value=18.0, max_value=50.0, value=32.0, step=0.5)
        
        with col_m3:
            length = st.number_input("Length", min_value=15.0, max_value=40.0, value=28.0, step=0.5)
        
        with col_m4:
            sleeves = st.number_input("Sleeves", min_value=16.0, max_value=40.0, value=32.0, step=0.5)
        
        # Fit
        fit = st.selectbox(
            "Fit",
            ["Slim", "Regular", "Relaxed", "Oversized"],
            key="fit"
        )
        
        # Material and Color
        col_mat, col_color = st.columns(2)
        with col_mat:
            material = st.selectbox(
                "Material",
                ["Cotton", "Linen", "Polyester", "Wool", "Silk", "Denim", "Cotton-Poly Blend"],
                key="material"
            )
        
        with col_color:
            color = st.text_input("Color", value="Black", key="color")
        
        # Additional preferences
        preferences = st.text_area(
            "Additional Preferences",
            placeholder="e.g., Add a design on the chest, stripes on sleeves...",
            height=100,
            key="preferences"
        )
        
        st.markdown("---")
        
        # Generate button
        generate_button = st.button(
            "✨ Generate Design",
            use_container_width=True,
            type="primary",
            key="generate_btn"
        )
    
    # Preview column
    with col2:
        st.subheader("🖼️ Your Custom Design")
        preview_placeholder = st.empty()
        prompt_placeholder = st.empty()
    
    # Handle generation
    if generate_button:
        with preview_placeholder.container():
            with st.spinner("🎨 Generating your custom design..."):
                try:
                    # Configure Gemini
                    configure(api_key=gemini_key)
                    # Try multiple model names for compatibility (newest first)
                    models_to_try = [
                        'gemini-flash-latest',  # Latest Gemini Flash (renamed)
                        'gemini-2.0-flash-exp',
                        'gemini-2.0-flash',
                        'gemini-exp-1206',
                        'gemini-1.5-flash-latest',
                        'gemini-1.5-flash',
                        'gemini-pro'
                    ]
                    
                    model = None
                    for model_name in models_to_try:
                        try:
                            model = GenerativeModel(model_name)
                            break  # Success, stop trying
                        except:
                            continue  # Try next model
                    
                    if not model:
                        raise ValueError("No available Gemini models found. Check your API key at https://aistudio.google.com")
                    
                    # Format measurements
                    measurements_text = f"""
                    Chest: {chest} inches
                    Waist: {waist} inches
                    Length: {length} inches
                    Sleeves: {sleeves} inches
                    Fit: {fit}
                    Color: {color}
                    Material: {material}
                    """
                    
                    # Generate prompt with Gemini
                    prompt_generation_input = f"""You are an expert fashion designer. Create a detailed, vivid image generation prompt for custom clothing based on these specifications:

MEASUREMENTS:
{measurements_text}

CLOTHING TYPE: {clothing_type}
STYLE: {style}
PREFERENCES: {preferences if preferences else 'No specific preferences'}

Generate a detailed prompt that will be used to create a realistic, high-quality image of the custom {clothing_type}. The prompt should:
1. Describe the fit based on the measurements (how snug, loose, tailored, etc.)
2. Include color, material, and texture details
3. Specify style elements and design details (pockets, buttons, seams, etc.)
4. Describe how it should appear on a model
5. Include lighting and photography style for best presentation

Make the prompt creative, specific, and suitable for an AI image generator. Focus on realistic fashion design presentation."""

                    response = model.generate_content(prompt_generation_input)
                    generated_prompt = response.text
                    
                    st.session_state.generated_prompt = generated_prompt
                    
                    # Generate image with Hugging Face
                    st.info("📸 Generating image... (this may take 1-2 minutes)")
                    
                    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
                    headers = {"Authorization": f"Bearer {hf_key}"}
                    
                    payload = {"inputs": generated_prompt}
                    
                    response = requests.post(API_URL, headers=headers, json=payload, timeout=120)
                    
                    if response.status_code == 200:
                        image = Image.open(BytesIO(response.content))
                        st.session_state.generated_image = image
                        st.success("✅ Design generated successfully!")
                    else:
                        st.error(f"❌ Image generation failed: {response.status_code}")
                        if response.status_code == 429:
                            st.warning("⚠️ Rate limited. Please wait a moment and try again.")
                        elif response.status_code == 400:
                            st.error("Invalid prompt. Please try adjusting your preferences.")
                
                except Exception as e:
                    error_msg = str(e)
                    st.error(f"❌ Error: {error_msg}")
                    
                    if "not found" in error_msg or "404" in error_msg:
                        st.error("❌ **Invalid Gemini API Key**\n\nYour API key is not working. Please:\n1. Go to https://aistudio.google.com\n2. Get a NEW API key\n3. Update it in Streamlit Secrets (Settings → Secrets)")
                    elif "API key" in error_msg or "UNAUTHENTICATED" in error_msg:
                        st.error("❌ **API Key Problem**\n\nYour Gemini API key is invalid or missing. Check:\n1. You copied the FULL key from aistudio.google.com\n2. No extra spaces at start/end\n3. It's added to Streamlit Cloud Secrets")
                    else:
                        st.info("💡 **Troubleshooting tips:**\n- Verify Gemini API key: https://aistudio.google.com\n- Verify Hugging Face token has read access\n- Free tier may have rate limits (wait a moment and retry)\n- Check both API keys in Streamlit Secrets (not in code)")
    
    # Display results
    if st.session_state.generated_image:
        with preview_placeholder.container():
            st.markdown('<div class="design-container">', unsafe_allow_html=True)
            st.image(st.session_state.generated_image, use_column_width=True)
            
            col_dl, col_buy = st.columns(2)
            with col_dl:
                # Download button
                img_buffer = BytesIO()
                st.session_state.generated_image.save(img_buffer, format="PNG")
                img_buffer.seek(0)
                
                st.download_button(
                    label="⬇️ Download Image",
                    data=img_buffer,
                    file_name="cozycraft-design.png",
                    mime="image/png"
                )
            
            with col_buy:
                if st.button("🛒 Continue to Purchase", use_container_width=True):
                    st.info("Purchase functionality can be integrated with Stripe, PayPal, etc.")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Display prompt
    if st.session_state.generated_prompt:
        with prompt_placeholder.container():
            with st.expander("📝 View Generation Prompt"):
                st.write(st.session_state.generated_prompt)

else:
    st.warning("👈 Please enter your API keys in the sidebar to get started!")
    
    st.markdown("""
    ## 🔑 How to Get Your API Keys (Free!)
    
    ### Google Gemini API
    1. Go to **[aistudio.google.com](https://aistudio.google.com)**
    2. Click **"Get API Key"**
    3. Click **"Create API key in new project"** 
    4. Copy the full key (including all characters)
    5. Paste it in the sidebar above
    
    ### Hugging  Face API Token
    1. Go to **[huggingface.co](https://huggingface.co)**
    2. Sign up (free, no credit card)
    3. Click your profile → **Settings**
    4. Click **"Access Tokens"** on left
    5. Click **"New token"** and select **"Read"**
    6. Copy and paste above
    
    🎉 **No credit card required!**
    
    ---
    
    ## 🚀 Deployed on Streamlit Cloud?
    
    If running this on Streamlit Cloud, add API keys to:
    1. Click app menu (⋮) → **Settings**
    2. Click **"Secrets"** tab
    3. Add both keys (without quotes):
    ```
    GEMINI_API_KEY = "your_key_here"
    HUGGINGFACE_API_KEY = "your_token_here"
    ```
    4. Click **"Save"**
    
    ---
    
    ## ❌ Getting "not found" or API errors?
    
    **Fix:** Your API key is wrong or expired.
    1. Get a FRESH key from the links above
    2. Make sure you copied the ENTIRE key (no spaces at start/end)
    3. Update it in Streamlit Cloud (**Settings → Secrets**)
    4. Refresh the page
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #999; font-size: 0.9rem;">
    🎨 CozyCraft | AI-Powered Custom Clothing Designer
</div>
""", unsafe_allow_html=True)
