export interface Scene {
  id: string;
  number: number;
  name: string;
  age: string;
  location: string;
  image: string;
  video: string | null;
  era: "childhood" | "teen" | "world";
}

export interface Era {
  id: "childhood" | "teen" | "world";
  label: string;
  subtitle: string;
  ageRange: string;
  startScene: number;
}

export const ERAS: Era[] = [
  { id: "childhood", label: "L'Enfance", subtitle: "Martinique", ageRange: "5 – 10 ans", startScene: 1 },
  { id: "teen", label: "L'Adolescence", subtitle: "France", ageRange: "15 – 18 ans", startScene: 4 },
  { id: "world", label: "Le Grand Voyage", subtitle: "Le Monde", ageRange: "25 – 30 ans", startScene: 6 },
];

export const SCENES: Scene[] = [
  {
    id: "scene_01_martinique_childhood",
    number: 1,
    name: "Les Premiers Pas",
    age: "5 ans",
    location: "Martinique",
    image: "/media/scene_01_martinique_childhood.png",
    video: "/media/scene_01_martinique_childhood.mp4",
    era: "childhood",
  },
  {
    id: "scene_02_martinique_carnival",
    number: 2,
    name: "Carnaval",
    age: "7 ans",
    location: "Martinique",
    image: "/media/scene_02_martinique_carnival.png",
    video: "/media/scene_02_martinique_carnival.mp4",
    era: "childhood",
  },
  {
    id: "scene_03_martinique_garden",
    number: 3,
    name: "Fleur des \u00celes",
    age: "10 ans",
    location: "Martinique",
    image: "/media/scene_03_martinique_garden.png",
    video: "/media/scene_03_martinique_garden.mp4",
    era: "childhood",
  },
  {
    id: "scene_04_limoges_winter",
    number: 4,
    name: "Hiver \u00e0 Limoges",
    age: "15 ans",
    location: "Limoges",
    image: "/media/scene_04_limoges_winter.png",
    video: "/media/scene_04_limoges_winter.mp4",
    era: "teen",
  },
  {
    id: "scene_06_paris_night",
    number: 5,
    name: "Nuits de Paris",
    age: "18 ans",
    location: "Paris",
    image: "/media/scene_06_paris_night.png",
    video: "/media/scene_06_paris_night.mp4",
    era: "teen",
  },
  {
    id: "scene_07_nyc_mets",
    number: 6,
    name: "Game Night",
    age: "25 ans",
    location: "New York",
    image: "/media/scene_07_nyc_mets.png",
    video: "/media/scene_07_nyc_mets.mp4",
    era: "world",
  },
  {
    id: "scene_08_nyc_sunset",
    number: 7,
    name: "Skyline Dor\u00e9e",
    age: "25 ans",
    location: "New York",
    image: "/media/scene_08_nyc_sunset.png",
    video: "/media/scene_08_nyc_sunset.mp4",
    era: "world",
  },
  {
    id: "scene_09_dubai_desert",
    number: 8,
    name: "Sable d\u2019Or",
    age: "26 ans",
    location: "Dubai",
    image: "/media/scene_09_dubai_desert.png",
    video: "/media/scene_09_dubai_desert.mp4",
    era: "world",
  },
  {
    id: "scene_10_sicily_cefalu",
    number: 9,
    name: "Dolce Vita",
    age: "26 ans",
    location: "Cefal\u00f9",
    image: "/media/scene_10_sicily_cefalu.png",
    video: "/media/scene_10_sicily_cefalu.mp4",
    era: "world",
  },
  {
    id: "scene_11_miami_beach",
    number: 10,
    name: "Ocean Drive",
    age: "27 ans",
    location: "Miami",
    image: "/media/scene_11_miami_beach.png",
    video: "/media/scene_11_miami_beach.mp4",
    era: "world",
  },
  {
    id: "scene_12_los_angeles",
    number: 11,
    name: "City of Angels",
    age: "27 ans",
    location: "Los Angeles",
    image: "/media/scene_12_los_angeles.png",
    video: "/media/scene_12_los_angeles.mp4",
    era: "world",
  },
  {
    id: "scene_13_yosemite",
    number: 12,
    name: "Wild & Free",
    age: "27 ans",
    location: "Yosemite",
    image: "/media/scene_13_yosemite.png",
    video: "/media/scene_13_yosemite.mp4",
    era: "world",
  },
  {
    id: "scene_14_monument_valley",
    number: 13,
    name: "Red Earth",
    age: "27 ans",
    location: "Monument Valley",
    image: "/media/scene_14_monument_valley.png",
    video: "/media/scene_14_monument_valley.mp4",
    era: "world",
  },
  {
    id: "scene_15_hawaii",
    number: 14,
    name: "Aloha",
    age: "28 ans",
    location: "Hawaii",
    image: "/media/scene_15_hawaii.png",
    video: "/media/scene_15_hawaii.mp4",
    era: "world",
  },
  {
    id: "scene_16_bali",
    number: 15,
    name: "Temple Sacr\u00e9",
    age: "28 ans",
    location: "Bali",
    image: "/media/scene_16_bali.png",
    video: "/media/scene_16_bali.mp4",
    era: "world",
  },
  {
    id: "scene_17_singapore",
    number: 16,
    name: "N\u00e9ons d\u2019Asie",
    age: "29 ans",
    location: "Singapore",
    image: "/media/scene_17_singapore.png",
    video: "/media/scene_17_singapore.mp4",
    era: "world",
  },
  {
    id: "scene_18_tokyo_disney",
    number: 17,
    name: "The Surprise",
    age: "30 ans",
    location: "Tokyo",
    image: "/media/scene_18_tokyo_disney.png",
    video: "/media/scene_18_tokyo_disney.mp4",
    era: "world",
  },
];
