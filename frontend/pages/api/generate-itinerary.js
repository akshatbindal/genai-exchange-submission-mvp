// This is a mock API endpoint. In a real application, this would proxy the request
// to the backend Python service.

const mockItineraries = [
  {
    title: 'The Adventurous Spirit',
    description: 'A trip focused on outdoor activities and exploration.',
    daily_plan: [
      { day: 1, activities: ['Arrival & Check-in', 'Explore the old town'], explanation: "Ease into your trip with a look at the local history." },
      { day: 2, activities: ['Mountain Hiking', 'Picnic by the lake'], explanation: "Chosen for your love of nature and adventure." },
      { day: 3, activities: ['Local Cooking Class', 'Evening market visit'], explanation: "A taste of the local culture, as you requested." },
    ],
    budget: 'Mid-range',
    booking_url: '#',
  },
  {
    title: 'The Cultural Connoisseur',
    description: 'Immerse yourself in the local art, history, and cuisine.',
    daily_plan: [
      { day: 1, activities: ['Art Museum Tour', 'Classical Music Concert'], explanation: "Perfect for art and history lovers." },
      { day: 2, activities: ['Historical walking tour', 'Wine tasting session'], explanation: "Discover the rich history and flavors of the region." },
      { day: 3, activities: ['Visit ancient ruins', 'Farewell dinner at a renowned local restaurant'], explanation: "A final look at the area's history, ending with a culinary highlight." },
    ],
    budget: 'Luxury',
    booking_url: '#',
  },
  {
    title: 'The Relaxation Getaway',
    description: 'A slow-paced journey designed for ultimate relaxation and rejuvenation.',
    daily_plan: [
        { day: 1, activities: ['Check into Spa Hotel', 'Relax by the pool'], explanation: "Start your unwinding journey immediately." },
        { day: 2, activities: ['Morning Yoga Session', 'Beach Day', 'Sunset Dinner'], explanation: "A full day dedicated to peace and beautiful views." },
        { day: 3, activities: ['Leisurely Brunch', 'Souvenir Shopping'], explanation: "A relaxed end to your perfect getaway." },
    ],
    budget: 'Budget-friendly',
    booking_url: '#',
  },
];


export default function handler(req, res) {
  if (req.method === 'POST') {
    // In a real app, you'd use the req.body to generate a personalized response.
    // For this MVP, we return the same mock data.
    // We simulate a network delay to make the loading state visible.
    setTimeout(() => {
      res.status(200).json({ itineraries: mockItineraries });
    }, 2000);
  } else {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
