import { SCENES, type Scene } from "./scenes";

export interface Location {
  name: string;
  x: number; // % from left
  y: number; // % from top
  scenes: Scene[];
}

// Positions computed via Robinson projection + IDW correction from 18 SVG reference points
// SVG viewBox: 30.767 241.591 784.077 458.627
// Robinson base params: cx=400.168 cy=520.294 sx=140.113 sy=240.951
// x_pct = (x_svg - 30.767) / 784.077 * 100, y_pct = (y_svg - 241.591) / 458.627 * 100
export const LOCATIONS: Location[] = [
  // Original timeline
  { name: "Martinique", x: 28.01, y: 50.47, scenes: [] },
  { name: "Limoges", x: 47.35, y: 31.06, scenes: [] },
  { name: "Paris", x: 47.69, y: 29.24, scenes: [] },
  { name: "New York", x: 26.08, y: 34.30, scenes: [] },
  { name: "Dubai", x: 63.61, y: 43.67, scenes: [] },
  { name: "Cefalù", x: 50.83, y: 35.99, scenes: [] },
  { name: "Miami", x: 23.03, y: 43.79, scenes: [] },
  { name: "Los Angeles", x: 12.63, y: 40.07, scenes: [] },
  { name: "Yosemite", x: 12.80, y: 37.64, scenes: [] },
  { name: "Monument Valley", x: 15.41, y: 38.04, scenes: [] },
  { name: "Hawaii", x: 1.5, y: 47.72, scenes: [] },
  { name: "Bali", x: 82.97, y: 68.32, scenes: [] },
  { name: "Singapore", x: 79.13, y: 60.54, scenes: [] },
  { name: "Tokyo", x: 87.18, y: 35.86, scenes: [] },
  // Friends timeline
  { name: "Hains Falls, NY", x: 25.2, y: 33.2, scenes: [] },
  { name: "Bryce Canyon", x: 14.8, y: 36.2, scenes: [] },
  { name: "Times Square, NYC", x: 27.0, y: 35.2, scenes: [] },
  { name: "Croatie", x: 52.0, y: 32.5, scenes: [] },
  { name: "Orlando, USA", x: 23.8, y: 41.5, scenes: [] },
  { name: "San Francisco", x: 11.2, y: 37.0, scenes: [] },
  { name: "Grand Canyon, USA", x: 14.2, y: 38.8, scenes: [] },
];

// Populate scenes into locations
for (const scene of SCENES) {
  const loc = LOCATIONS.find((l) => l.name === scene.location);
  if (loc) loc.scenes.push(scene);
}
