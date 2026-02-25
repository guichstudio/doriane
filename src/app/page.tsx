"use client";

import { useState } from "react";
import { AnimatePresence } from "framer-motion";
import ErrorBoundary from "@/components/ErrorBoundary";
import IntroScreen from "@/components/IntroScreen";
import WorldMap from "@/components/WorldMap";
import StoryFlow from "@/components/StoryFlow";

type Screen = "intro" | "worldmap" | "story";

export default function Home() {
  const [screen, setScreen] = useState<Screen>("intro");
  const [initialScene, setInitialScene] = useState<number | null>(null);

  const handleEnter = () => setScreen("worldmap");

  const handleSelectScene = (sceneIndex: number) => {
    setInitialScene(sceneIndex);
    setScreen("story");
  };

  const handleStart = () => {
    setInitialScene(null);
    setScreen("story");
  };

  return (
    <ErrorBoundary>
      <main className="min-h-screen bg-background">
        <AnimatePresence mode="wait">
          {screen === "intro" && (
            <IntroScreen key="intro" onEnter={handleEnter} />
          )}
          {screen === "worldmap" && (
            <WorldMap
              key="worldmap"
              onSelectScene={handleSelectScene}
              onStart={handleStart}
            />
          )}
        </AnimatePresence>

        {screen === "story" && (
            <StoryFlow
              initialScene={initialScene}
              onBack={() => setScreen("worldmap")}
            />
          )}
      </main>
    </ErrorBoundary>
  );
}
