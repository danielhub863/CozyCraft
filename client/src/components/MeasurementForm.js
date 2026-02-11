import React, { useState } from 'react';
import '../styles/MeasurementForm.css';

const CLOTHING_TYPES = [
  'T-Shirt',
  'Button-Up Shirt',
  'Sweater',
  'Hoodie',
  'Dress',
  'Pants',
  'Shorts',
  'Jacket',
  'Coat',
  'Skirt'
];

const STYLES = [
  'Casual',
  'Formal',
  'Athletic',
  'Vintage',
  'Modern',
  'Bohemian',
  'Minimalist',
  'Streetwear',
  'Elegant'
];

function MeasurementForm({ onSubmit, loading }) {
  const [formData, setFormData] = useState({
    clothingType: 'T-Shirt',
    style: 'Casual',
    color: 'Black',
    material: 'Cotton',
    chest: '38',
    waist: '32',
    length: '28',
    sleeves: '32',
    fit: 'Regular',
    preferences: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Prepare measurements object
    const measurements = {
      chest: `${formData.chest} inches`,
      waist: `${formData.waist} inches`,
      length: `${formData.length} inches`,
      sleeves: `${formData.sleeves} inches`,
      fit: formData.fit,
      color: formData.color,
      material: formData.material
    };

    onSubmit({
      measurements,
      clothingType: formData.clothingType,
      style: formData.style,
      preferences: formData.preferences,
      fit: formData.fit
    });
  };

  return (
    <form className="measurement-form" onSubmit={handleSubmit}>
      <h2>📐 Your Measurements</h2>

      {/* Clothing Type */}
      <div className="form-group">
        <label htmlFor="clothingType">Clothing Type *</label>
        <select
          id="clothingType"
          name="clothingType"
          value={formData.clothingType}
          onChange={handleChange}
          required
        >
          {CLOTHING_TYPES.map(type => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>
      </div>

      {/* Style */}
      <div className="form-group">
        <label htmlFor="style">Style</label>
        <select
          id="style"
          name="style"
          value={formData.style}
          onChange={handleChange}
        >
          {STYLES.map(s => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
      </div>

      {/* Measurements Section */}
      <div className="measurements-grid">
        <div className="form-group">
          <label htmlFor="chest">Chest (inches) *</label>
          <input
            type="number"
            id="chest"
            name="chest"
            value={formData.chest}
            onChange={handleChange}
            min="20"
            max="60"
            step="0.5"
            required
            placeholder="e.g., 38"
          />
        </div>

        <div className="form-group">
          <label htmlFor="waist">Waist (inches) *</label>
          <input
            type="number"
            id="waist"
            name="waist"
            value={formData.waist}
            onChange={handleChange}
            min="18"
            max="50"
            step="0.5"
            required
            placeholder="e.g., 32"
          />
        </div>

        <div className="form-group">
          <label htmlFor="length">Length (inches) *</label>
          <input
            type="number"
            id="length"
            name="length"
            value={formData.length}
            onChange={handleChange}
            min="15"
            max="40"
            step="0.5"
            required
            placeholder="e.g., 28"
          />
        </div>

        <div className="form-group">
          <label htmlFor="sleeves">Sleeve Length (inches)</label>
          <input
            type="number"
            id="sleeves"
            name="sleeves"
            value={formData.sleeves}
            onChange={handleChange}
            min="16"
            max="40"
            step="0.5"
            placeholder="e.g., 32"
          />
        </div>
      </div>

      {/* Fit */}
      <div className="form-group">
        <label htmlFor="fit">Fit</label>
        <select
          id="fit"
          name="fit"
          value={formData.fit}
          onChange={handleChange}
        >
          <option value="Slim">Slim Fit</option>
          <option value="Regular">Regular Fit</option>
          <option value="Relaxed">Relaxed Fit</option>
          <option value="Oversized">Oversized Fit</option>
        </select>
      </div>

      {/* Material & Color */}
      <div className="form-row">
        <div className="form-group">
          <label htmlFor="material">Material</label>
          <select
            id="material"
            name="material"
            value={formData.material}
            onChange={handleChange}
          >
            <option value="Cotton">Cotton</option>
            <option value="Linen">Linen</option>
            <option value="Polyester">Polyester</option>
            <option value="Wool">Wool</option>
            <option value="Silk">Silk</option>
            <option value="Denim">Denim</option>
            <option value="Blend">Cotton-Poly Blend</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="color">Color</label>
          <input
            type="text"
            id="color"
            name="color"
            value={formData.color}
            onChange={handleChange}
            placeholder="e.g., Navy Blue, Burgundy"
          />
        </div>
      </div>

      {/* Additional Preferences */}
      <div className="form-group">
        <label htmlFor="preferences">Additional Preferences</label>
        <textarea
          id="preferences"
          name="preferences"
          value={formData.preferences}
          onChange={handleChange}
          placeholder="e.g., Add a design on the chest, stripes on sleeves, etc."
          rows="3"
        />
      </div>

      <button
        type="submit"
        disabled={loading}
        className="submit-button"
      >
        {loading ? 'Generating Design...' : '✨ Generate Design'}
      </button>
    </form>
  );
}

export default MeasurementForm;
