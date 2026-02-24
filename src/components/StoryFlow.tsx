"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { motion } from "framer-motion";
import { SCENES, ERAS } from "@/lib/scenes";
import SceneBlock from "./SceneBlock";
import ChapterDivider from "./ChapterDivider";
import Timeline from "./Timeline";
import Finale from "./Finale";

export default function StoryFlow() {
  const [activeIndex, setActiveIndex] = useState(0);
  const sceneRefs = useRef<Map<string, HTMLElement>>(new Map());

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
