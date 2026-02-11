import { GoogleGenerativeAI } from '@google/generative-ai';

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

export async function generatePrompt({ measurements, clothingType, style, preferences }) {
  try {
    const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

    const measurementsText = formatMeasurements(measurements);
    const preferencesText = preferences ? formatPreferences(preferences) : 'No specific preferences';

    const prompt = `You are an expert fashion designer. Create a detailed, vivid image generation prompt for custom clothing based on these specifications:

MEASUREMENTS:
${measurementsText}

CLOTHING TYPE: ${clothingType}
STYLE: ${style || 'Modern'}
PREFERENCES: ${preferencesText}

Generate a detailed prompt that will be used to create a realistic, high-quality image of the custom ${clothingType}. The prompt should:
1. Describe the fit based on the measurements (how snug, loose, tailored, etc.)
2. Include color, material, and texture details
3. Specify style elements and design details (pockets, buttons, seams, etc.)
4. Describe how it should appear on a model
5. Include lighting and photography style for best presentation

Make the prompt creative, specific, and suitable for an AI image generator. Focus on realistic fashion design presentation.`;

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const generatedPrompt = response.text();

    return generatedPrompt;
  } catch (error) {
    console.error('Error generating prompt:', error);
    throw new Error(`Failed to generate prompt: ${error.message}`);
  }
}

function formatMeasurements(measurements) {
  if (typeof measurements === 'string') {
    return measurements;
  }

  if (typeof measurements === 'object') {
    return Object.entries(measurements)
      .map(([key, value]) => `${key}: ${value}`)
      .join('\n');
  }

  return String(measurements);
}

function formatPreferences(preferences) {
  if (typeof preferences === 'string') {
    return preferences;
  }

  if (Array.isArray(preferences)) {
    return preferences.join(', ');
  }

  if (typeof preferences === 'object') {
    return Object.entries(preferences)
      .map(([key, value]) => `${key}: ${value}`)
      .join(', ');
  }

  return String(preferences);
}
