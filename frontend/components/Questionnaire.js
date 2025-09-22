import { useState } from 'react';
import styles from './Questionnaire.module.css';

export default function Questionnaire({ onSubmit }) {
  const [answers, setAnswers] = useState({
    destination: '',
    tripType: 'Relaxation',
    interests: [],
    budget: 'Mid-range',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setAnswers({ ...answers, [name]: value });
  };

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    let newInterests = [...answers.interests];
    if (checked) {
      newInterests.push(name);
    } else {
      newInterests = newInterests.filter((interest) => interest !== name);
    }
    setAnswers({ ...answers, interests: newInterests });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(answers);
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <div className={styles.formGroup}>
        <label htmlFor="destination">Where do you want to go?</label>
        <input
          type="text"
          id="destination"
          name="destination"
          value={answers.destination}
          onChange={handleInputChange}
          placeholder="e.g., Paris, France"
          required
        />
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="tripType">What's the main goal of your trip?</label>
        <select id="tripType" name="tripType" value={answers.tripType} onChange={handleInputChange}>
          <option>Relaxation</option>
          <option>Adventure</option>
          <option>Cultural</option>
          <option>Romantic</option>
        </select>
      </div>

      <div className={styles.formGroup}>
        <label>What are your interests?</label>
        <div className={styles.checkboxGroup}>
          <label><input type="checkbox" name="History" onChange={handleCheckboxChange} /> History</label>
          <label><input type="checkbox" name="Art & Museums" onChange={handleCheckboxChange} /> Art & Museums</label>
          <label><input type="checkbox" name="Food & Cuisine" onChange={handleCheckboxChange} /> Food & Cuisine</label>
          <label><input type="checkbox" name="Nightlife" onChange={handleCheckboxChange} /> Nightlife</label>
          <label><input type="checkbox" name="Nature & Outdoors" onChange={handleCheckboxChange} /> Nature & Outdoors</label>
          <label><input type="checkbox" name="Shopping" onChange={handleCheckboxChange} /> Shopping</label>
        </div>
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="budget">What's your budget?</label>
        <select id="budget" name="budget" value={answers.budget} onChange={handleInputChange}>
          <option>Budget-friendly</option>
          <option>Mid-range</option>
          <option>Luxury</option>
        </select>
      </div>

      <button type="submit" className={styles.submitButton}>Generate My Itinerary</button>
    </form>
  );
}
