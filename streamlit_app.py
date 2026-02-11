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
        replicate_key = st.secrets["REPLICATE_API_KEY"]
        st.success("✅ API Keys loaded from Streamlit Secrets")
    except (KeyError, FileNotFoundError):
        st.info("📝 Using manual API key input (local development)")
        
        gemini_key = st.text_input(
            "Google Gemini API Key",
            type="password",
            help="Get from: https://aistudio.google.com"
        )
        
        replicate_key = st.text_input(
            "Replicate API Token",
            type="password",
            help="Get from: https://replicate.com/account/api-tokens"
        )

# Main app
if gemini_key and replicate_key:
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
                    
                    # Generate image with Replicate API
                    st.info("📸 Generating image with Replicate... (this may take 1-2 minutes)")
                    
                    import time
                    
                    headers = {"Authorization": f"Token {replicate_key}"}
                    
                    try:
                        with st.spinner("🎨 Starting image generation..."):
                            # Create prediction on Replicate
                            response = requests.post(
                                "https://api.replicate.com/v1/predictions",
                                headers=headers,
                                json={
                                    "version": "8fda5fdf3367688b19e56887cd97069e0b0b2b79",  # Stable Diffusion 3
                                    "input": {"prompt": generated_prompt}
                                },
                                timeout=30
                            )
                        
                        if response.status_code == 201:
                            prediction = response.json()
                            prediction_id = prediction['id']
                            
                            # Poll for completion
                            max_wait = 300  # 5 minutes
                            elapsed = 0
                            poll_interval = 2
                            
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            with st.spinner("⏳ Waiting for image generation to complete..."):
                                while elapsed < max_wait:
                                    poll_response = requests.get(
                                        f"https://api.replicate.com/v1/predictions/{prediction_id}",
                                        headers=headers
                                    )
                                    
                                    if poll_response.status_code == 200:
                                        pred_data = poll_response.json()
                                        progress = min(elapsed / max_wait, 0.99)
                                        progress_bar.progress(progress)
                                        status_text.text(f"Status: {pred_data['status']}...")
                                        
                                        if pred_data['status'] == 'succeeded':
                                            image_url = pred_data['output'][0]
                                            img_response = requests.get(image_url)
                                            image = Image.open(BytesIO(img_response.content))
                                            st.session_state.generated_image = image
                                            progress_bar.progress(1.0)
                                            status_text.text("✅ Image generated successfully!")
                                            st.success("✅ Success! Image generated with Stable Diffusion 3")
                                            break
                                        elif pred_data['status'] == 'failed':
                                            error_msg = pred_data.get('error', 'Unknown error')
                                            st.error(f"❌ Image generation failed: {error_msg}")
                                            break
                                    
                                    time.sleep(poll_interval)
                                    elapsed += poll_interval
                            
                            progress_bar.empty()
                            status_text.empty()
                            
                            if elapsed >= max_wait:
                                st.warning("⏳ Image generation took too long. Please try again.")
                        
                        elif response.status_code == 401:
                            st.error("❌ **Invalid Replicate API Token**\\n\\nCheck your token in Streamlit Secrets")
                        elif response.status_code == 400:
                            st.error(f"❌ **Bad Request**: {response.json().get('detail', 'Invalid parameters')}")
                        else:
                            st.error(f"❌ **Error {response.status_code}**: {response.text}")
                    
                    except Exception as e:
                        image_generated = False
                        last_error = str(e)
                        st.error(f"❌ Error generating image: {last_error}")
                        st.info("💡 **Troubleshooting:**\n"
                               "• Check Replicate token at: https://replicate.com/account/api-tokens\n"
                               "• Ensure you have credits in your Replicate account\n"
                               "• Try a different prompt\n"
                               "• Check Replicate status: https://status.replicate.com")
                
                except Exception as e:
                    error_msg = str(e)
                    st.error(f"❌ Error: {error_msg}")
                    
                    if "not found" in error_msg or "404" in error_msg:
                        st.error("❌ **Invalid Gemini API Key**\n\nYour API key is not working. Please:\n1. Go to https://aistudio.google.com\n2. Get a NEW API key\n3. Update it in Streamlit Secrets (Settings → Secrets)")
                    elif "API key" in error_msg or "UNAUTHENTICATED" in error_msg:
                        st.error("❌ **API Key Problem**\n\nYour Gemini API key is invalid or missing. Check:\n1. You copied the FULL key from aistudio.google.com\n2. No extra spaces at start/end\n3. It's added to Streamlit Cloud Secrets")
                    else:
                        st.info("💡 **Troubleshooting tips:**\n- Verify Gemini API key: https://aistudio.google.com\n- Verify Replicate token at: https://replicate.com/account/api-tokens\n- Ensure you have credits in Replicate account\n- Check both API keys in Streamlit Secrets (not in code)")
    
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
    
    ### Replicate API Token
    1. Go to **[replicate.com](https://replicate.com)**
    2. Sign up (free account with free credits)
    3. Click your profile → **Account**
    4. Scroll down to **"API tokens"**
    5. Copy your API token
    6. Paste it in the sidebar above
    
    💡 **Free tier includes credits for image generation!**
    
    ---
    
    ## 🚀 Deployed on Streamlit Cloud?
    
    If running this on Streamlit Cloud, add API keys to:
    1. Click app menu (⋮) → **Settings**
    2. Click **"Secrets"** tab
    3. Add both keys (without quotes):
    ```
    GEMINI_API_KEY = "your_key_here"
    REPLICATE_API_KEY = "your_token_here"
    ```
    4. Click **"Save"**
    
    ---
    
    ## ❌ Getting errors?
    
    **Fix:** Your API key is wrong, expired, or Replicate account has no credits.
    1. Get FRESH keys from the links above
    2. Check Replicate account has available credits: https://replicate.com/account/api-tokens
    3. Make sure you copied the ENTIRE key (no spaces at start/end)
    4. Update it in Streamlit Cloud (**Settings → Secrets**)
    5. Refresh the page
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #999; font-size: 0.9rem;">
    🎨 CozyCraft | AI-Powered Custom Clothing Designer
</div>
""", unsafe_allow_html=True)
