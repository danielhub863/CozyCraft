import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 180000, // 3 minutes timeout
});

export async function generateDesign(formData) {
  try {
    const response = await apiClient.post('/api/design-clothing', {
      measurements: formData.measurements,
      clothingType: formData.clothingType,
      style: formData.style,
      preferences: formData.preferences
    });

    if (response.data.success) {
      return {
        imageUrl: response.data.imageUrl,
        prompt: response.data.prompt,
        design: response.data.design
      };
    } else {
      throw new Error('Design generation failed');
    }
  } catch (error) {
    if (error.response?.data?.message) {
      throw new Error(error.response.data.message);
    }
    throw new Error(error.message || 'Failed to generate design');
  }
}

export async function generatePrompt(formData) {
  try {
    const response = await apiClient.post('/api/generate-prompt', {
      measurements: formData.measurements,
      clothingType: formData.clothingType,
      style: formData.style,
      preferences: formData.preferences
    });

    if (response.data.success) {
      return response.data.prompt;
    } else {
      throw new Error('Prompt generation failed');
    }
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message);
  }
}

export async function generateImage(prompt) {
  try {
    const response = await apiClient.post('/api/generate-image', {
      prompt
    });

    if (response.data.success) {
      return response.data.imageUrl;
    } else {
      throw new Error('Image generation failed');
    }
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message);
  }
}

export async function checkServerHealth() {
  try {
    const response = await apiClient.get('/api/health');
    return response.data;
  } catch (error) {
    throw new Error('Server is not responding');
  }
}
