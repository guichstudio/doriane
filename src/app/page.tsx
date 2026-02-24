"use client";

import { useState } from "react";
import { AnimatePresence } from "framer-motion";
import IntroScreen from "@/components/IntroScreen";
import StoryFlow from "@/components/StoryFlow";

export default function Home() {
  const [showIntro, setShowIntro] = useState(true);

  return (
    <main className="min-h-screen bg-background">
      <AnimatePresence mode="wait">
        {showIntro && (
          <IntroScreen key="intro" onEnter={() => setShowIntro(false)} />
        )}
      </AnimatePresence>

      {!showIntro && <StoryFlow />}
    </main>
  );
}
