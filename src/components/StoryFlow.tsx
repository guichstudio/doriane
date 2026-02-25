"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { motion } from "framer-motion";
import { SCENES, ERAS } from "@/lib/scenes";
import SceneBlock from "./SceneBlock";
import ChapterDivider from "./ChapterDivider";
import Timeline from "./Timeline";
import Finale from "./Finale";

export default function StoryFlow({
  initialScene,
  onBack,
}: {
  initialScene?: number | null;
  onBack?: () => void;
}) {
  const [activeIndex, setActiveIndex] = useState(0);
  const sceneRefs = useRef<Map<string, HTMLElement>>(new Map());

  // Scroll to initial scene if selected from world map
  useEffect(() => {
    if (initialScene != null && initialScene >= 0 && initialScene < SCENES.length) {
      const target = document.getElementById(SCENES[initialScene].id);
      if (target) {
        // Small delay to ensure DOM is ready
        setTimeout(() => target.scrollIntoView({ behavior: "instant" }), 100);
      }
    }
  }, [initialScene]);

  // Track which scene is currently in the center of the viewport
  useEffect(() => {
    const observers: IntersectionObserver[] = [];

    SCENES.forEach((scene, i) => {
      const el = document.getElementById(scene.id);
      if (!el) return;

      const observer = new IntersectionObserver(
        ([entry]) => {
          if (entry.isIntersecting) {
            setActiveIndex(i);
          }
        },
        { threshold: 0.5 }
      );

      observer.observe(el);
      observers.push(observer);
    });

    return () => observers.forEach((o) => o.disconnect());
  }, []);

  // Group scenes by era to insert chapter dividers
  const eraStartScenes = new Set(ERAS.map((e) => e.startScene));

  return (
    <motion.div
      className="relative"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.6 }}
    >
      <Timeline activeIndex={activeIndex} />

      {/* Back to world map */}
      {onBack && (
        <motion.button
          onClick={onBack}
          className="fixed top-6 left-6 z-50 flex items-center gap-2 px-4 py-2 rounded-full
                     border border-pink/30 bg-black/60 backdrop-blur-sm text-pink text-xs
                     tracking-[0.1em] uppercase hover:bg-pink/10 transition-colors cursor-pointer"
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.5, duration: 0.4 }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <span>←</span>
          <span>Map</span>
        </motion.button>
      )}

      <div className="snap-y snap-mandatory">
        {SCENES.map((scene, i) => {
          const era = ERAS.find((e) => e.startScene === scene.number);
          return (
            <div key={scene.id}>
              {era && <ChapterDivider era={era} />}
              <SceneBlock scene={scene} index={i} />
            </div>
          );
        })}

        <Finale />
      </div>
    </motion.div>
  );
}
