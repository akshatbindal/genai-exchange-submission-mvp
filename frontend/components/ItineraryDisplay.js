import styles from './ItineraryDisplay.module.css';

export default function ItineraryDisplay({ itineraries }) {
  if (!itineraries || itineraries.length === 0) {
    return <p>No itineraries to display.</p>;
  }

  return (
    <div className={styles.container}>
      <h2 className={styles.header}>Your Personalized Itineraries</h2>
      <div className={styles.itinerariesGrid}>
        {itineraries.map((itinerary, index) => (
          <div key={index} className={styles.itineraryCard}>
            <h3 className={styles.itineraryTitle}>{itinerary.title}</h3>
            <p className={styles.itineraryDescription}>{itinerary.description}</p>
            <div className={styles.details}>
              <h4>Daily Plan:</h4>
              <ul>
                {itinerary.daily_plan.map((day, dayIndex) => (
                  <li key={dayIndex}>
                    <strong>Day {day.day}:</strong> {day.activities.join(', ')}
                    <p className={styles.explanation}>{day.explanation}</p>
                  </li>
                ))}
              </ul>
              <div className={styles.bookingInfo}>
                <p><strong>Budget:</strong> {itinerary.budget}</p>
                <a href={itinerary.booking_url} target="_blank" rel="noopener noreferrer" className={styles.bookingLink}>Book Now</a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
