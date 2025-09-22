import Head from 'next/head';
import { useState } from 'react';
import Questionnaire from '../components/Questionnaire';
import ItineraryDisplay from '../components/ItineraryDisplay';
import styles from '../styles/Home.module.css';

export default function Home() {
  const [itineraries, setItineraries] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (answers) => {
    setIsLoading(true);
    setError(null);
    setItineraries(null);

    try {
      // The API endpoint will be created in a later step
      const response = await fetch('/api/generate-itinerary', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers),
      });

      if (!response.ok) {
        throw new Error('Failed to generate itinerary. Please try again.');
      }

      const data = await response.json();
      setItineraries(data.itineraries);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>AI Personal Travel Agent</title>
        <meta name="description" content="Your personal AI-powered travel planner" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Your Personal Trip Architect
        </h1>

        <p className={styles.description}>
          Tell us about your ideal trip, and we'll craft the perfect itinerary for you.
        </p>

        {!itineraries && !isLoading && <Questionnaire onSubmit={handleSubmit} />}

        {isLoading && <p>Generating your personalized itineraries... this may take a moment.</p>}

        {error && <p className={styles.error}>{error}</p>}

        {itineraries && <ItineraryDisplay itineraries={itineraries} />}
      </main>
    </div>
  );
}
