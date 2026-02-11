import axios from 'axios';

const HF_API_URL = 'https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large';

export async function generateImage(prompt) {
  try {
    if (!process.env.HUGGINGFACE_API_KEY) {
      throw new Error('HUGGINGFACE_API_KEY is not set');
    }

    const response = await axios.post(
      HF_API_URL,
      { inputs: prompt },
      {
        headers: {
          Authorization: `Bearer ${process.env.HUGGINGFACE_API_KEY}`,
          'Content-Type': 'application/json'
        },
        responseType: 'arraybuffer',
        timeout: 120000 // 2 minutes timeout for image generation
      }
    );

    // Convert image buffer to base64
    const imageBuffer = Buffer.from(response.data);
    const base64Image = imageBuffer.toString('base64');
    const mimeType = response.headers['content-type'] || 'image/jpeg';
    const imageUrl = `data:${mimeType};base64,${base64Image}`;

    return imageUrl;
  } catch (error) {
    console.error('Error generating image:', error.message);

    // Provide more helpful error messages
    if (error.response?.status === 429) {
      throw new Error('Rate limited by Hugging Face. Please try again in a moment.');
    } else if (error.response?.status === 400) {
      throw new Error('Invalid prompt. Please revise and try again.');
    } else if (error.message.includes('timeout')) {
      throw new Error('Image generation took too long. Please try again.');
    }

    throw new Error(`Failed to generate image: ${error.message}`);
  }
}

// Alternative: Using a different model if needed
export async function generateImageAlternative(prompt) {
  try {
    const modelUrl = 'https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5';

    const response = await axios.post(
      modelUrl,
      { inputs: prompt },
      {
        headers: {
          Authorization: `Bearer ${process.env.HUGGINGFACE_API_KEY}`,
          'Content-Type': 'application/json'
        },
        responseType: 'arraybuffer',
        timeout: 120000
      }
    );

    const imageBuffer = Buffer.from(response.data);
    const base64Image = imageBuffer.toString('base64');
    const mimeType = 'image/jpeg';
    const imageUrl = `data:${mimeType};base64,${base64Image}`;

    return imageUrl;
  } catch (error) {
    console.error('Error generating alternative image:', error.message);
    throw new Error(`Failed to generate alternative image: ${error.message}`);
  }
}
