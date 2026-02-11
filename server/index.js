import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { generatePrompt } from './services/promptGenerator.js';
import { generateImage } from './services/imageGenerator.js';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors({
  origin: process.env.CORS_ORIGIN || 'http://localhost:3000'
}));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ limit: '50mb', extended: true }));

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'Server is running' });
});

// Generate prompt endpoint
app.post('/api/generate-prompt', async (req, res) => {
  try {
    const { measurements, clothingType, style, preferences } = req.body;

    if (!measurements || !clothingType) {
      return res.status(400).json({
        error: 'Missing required fields: measurements and clothingType'
      });
    }

    const prompt = await generatePrompt({
      measurements,
      clothingType,
      style,
      preferences
    });

    res.json({ prompt, success: true });
  } catch (error) {
    console.error('Prompt generation error:', error);
    res.status(500).json({
      error: 'Failed to generate prompt',
      message: error.message
    });
  }
});

// Generate image endpoint
app.post('/api/generate-image', async (req, res) => {
  try {
    const { prompt } = req.body;

    if (!prompt) {
      return res.status(400).json({
        error: 'Missing required field: prompt'
      });
    }

    const imageUrl = await generateImage(prompt);

    res.json({ imageUrl, success: true });
  } catch (error) {
    console.error('Image generation error:', error);
    res.status(500).json({
      error: 'Failed to generate image',
      message: error.message
    });
  }
});

// Combined endpoint: measurements -> prompt -> image
app.post('/api/design-clothing', async (req, res) => {
  try {
    const { measurements, clothingType, style, preferences } = req.body;

    if (!measurements || !clothingType) {
      return res.status(400).json({
        error: 'Missing required fields: measurements and clothingType'
      });
    }

    // Step 1: Generate prompt from measurements
    const prompt = await generatePrompt({
      measurements,
      clothingType,
      style,
      preferences
    });

    // Step 2: Generate image from prompt
    const imageUrl = await generateImage(prompt);

    res.json({
      success: true,
      prompt,
      imageUrl,
      design: {
        clothingType,
        style,
        measurements
      }
    });
  } catch (error) {
    console.error('Design generation error:', error);
    res.status(500).json({
      error: 'Failed to generate design',
      message: error.message
    });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({
    error: 'Internal server error',
    message: err.message
  });
});

app.listen(PORT, () => {
  console.log(`🎨 CozyCraft Server running on http://localhost:${PORT}`);
});
