import React from 'react';
import '../styles/DesignPreview.css';

function DesignPreview({ imageUrl, prompt }) {
  const downloadImage = () => {
    if (!imageUrl) return;

    const link = document.createElement('a');
    link.href = imageUrl;
    link.download = `cozycraft-design-${new Date().getTime()}.jpg`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="design-preview">
      <h2>🖼️ Your Custom Design</h2>

      {imageUrl && (
        <div className="preview-container">
          <img src={imageUrl} alt="Generated clothing design" className="design-image" />

          <div className="preview-actions">
            <button onClick={downloadImage} className="action-button download-button">
              ⬇️ Download Image
            </button>
            <button className="action-button purchase-button">
              🛒 Continue to Purchase
            </button>
          </div>
        </div>
      )}

      {prompt && (
        <div className="prompt-details">
          <details>
            <summary>📝 View Generation Prompt</summary>
            <p className="prompt-text">{prompt}</p>
          </details>
        </div>
      )}
    </div>
  );
}

export default DesignPreview;
