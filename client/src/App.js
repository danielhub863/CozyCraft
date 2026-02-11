import React, { useState } from 'react';
import MeasurementForm from './components/MeasurementForm';
import DesignPreview from './components/DesignPreview';
import { generateDesign } from './services/api';
import './App.css';

function App() {
  const [design, setDesign] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [prompt, setPrompt] = useState(null);

  const handleGenerateDesign = async (formData) => {
    setLoading(true);
    setError(null);
    setPrompt(null);
    setDesign(null);

    try {
      const result = await generateDesign(formData);
      setDesign(result.imageUrl);
      setPrompt(result.prompt);
    } catch (err) {
      setError(err.message || 'Failed to generate design. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🎨 CozyCraft</h1>
        <p>Design Your Perfect Custom Clothing</p>
      </header>

      <div className="app-container">
        <div className="form-section">
          <MeasurementForm
            onSubmit={handleGenerateDesign}
            loading={loading}
          />
        </div>

        <div className="preview-section">
          {error && (
            <div className="error-message">
              <h3>⚠️ Error</h3>
              <p>{error}</p>
            </div>
          )}

          {loading && (
            <div className="loading-container">
              <div className="spinner"></div>
              <p>Generating your custom design...</p>
              <small>This may take a moment</small>
            </div>
          )}

          {design && !loading && (
            <DesignPreview
              imageUrl={design}
              prompt={prompt}
              formData={null}
            />
          )}

          {!design && !loading && !error && (
            <div className="empty-state">
              <p>Fill in your measurements and clothing preferences to generate a custom design</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
