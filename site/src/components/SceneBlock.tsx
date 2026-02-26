"use client";

import { useRef, useEffect, useState } from "react";
import { motion, useInView } from "framer-motion";
import type { Scene } from "@/lib/scenes";

function PlayIcon() {
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      className="w-16 h-16 drop-shadow-lg"
    >
      <circle cx="32" cy="32" r="31" fill="rgba(0,0,0,0.45)" stroke="rgba(255,255,255,0.8)" strokeWidth="2" />
      <path d="M26 20L46 32L26 44V20Z" fill="rgba(255,255,255,0.9)" />
    </svg>
  );
}

export default function SceneBlock({
  scene,
  index,
}: {
  scene: Scene;
  index: number;
}) {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const isInView = useInView(containerRef, { amount: 0.3 });
  const isNear = useInView(containerRef, { margin: "200% 0px 200% 0px" });
  const [preload, setPreload] = useState<"none" | "metadata">("none");
  const [isMobile, setIsMobile] = useState(false);

  // Detect mobile on mount
  useEffect(() => {
    const check = () => setIsMobile(window.innerWidth < 768);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);

  // Preload when near viewport (desktop only)
  useEffect(() => {
    if (isNear && !isMobile) setPreload("metadata");
  }, [isNear, isMobile]);

  // Play/pause video based on viewport visibility (desktop only)
  useEffect(() => {
    if (isMobile) return;
    const video = videoRef.current;
    if (!video) return;
    if (isInView) {
      video.play().catch(() => {});
    } else {
      video.pause();
      video.currentTime = 0;
    }
  }, [isInView, isMobile]);

  // Mobile: tap image → open video in native fullscreen player
  const handleMobileTap = () => {
    if (!scene.video) return;
    // Open video directly — mobile browsers open native player
    window.open(scene.video, "_blank");
  };

  const numberStr = String(scene.number).padStart(2, "0");
  const isFriends = scene.era === "friends";

  return (
    <div
      ref={containerRef}
      id={scene.id}
      className="relative h-screen-safe w-full overflow-hidden snap-start"
    >
      {/* Desktop: auto-playing video */}
      {!isMobile && scene.video ? (
        <video
          ref={videoRef}
          src={scene.video}
          poster={scene.image}
          muted
          loop
          playsInline
          preload={preload}
          className="scene-media"
        />
      ) : (
        /* Mobile: image with play button overlay, or image-only scene */
        <>
          <img
            src={scene.image}
            alt={scene.name}
            className="scene-media"
          />
          {/* Play button — mobile only, only if video exists */}
          {isMobile && scene.video && (
            <button
              onClick={handleMobileTap}
              className="absolute inset-0 z-[5] flex items-center justify-center cursor-pointer"
              aria-label="Lire la vidéo"
            >
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: 0.5 }}
              >
                <PlayIcon />
              </motion.div>
            </button>
          )}
        </>
      )}

      {/* Bottom gradient overlay */}
      <div className="scene-overlay absolute inset-0 pointer-events-none" />

      {/* Text overlay — safe area aware */}
      <div className="absolute bottom-0 left-0 right-0 p-6 pb-8 sm:p-8 sm:pb-10 md:p-12 md:pl-24 z-10 safe-bottom">
        <motion.p
          className={`${isFriends ? "scene-number-purple" : "scene-number"} mb-1.5 sm:mb-2`}
          initial={{ opacity: 0, y: 15 }}
          whileInView={{ opacity: 0.6, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.5, delay: 0.1 }}
        >
          {numberStr}
        </motion.p>

        <motion.h2
          className={`${isFriends ? "gta-title-purple" : "gta-title"} text-3xl sm:text-5xl md:text-6xl mb-2 sm:mb-3`}
          initial={{ opacity: 0, y: 15 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          {scene.name}
        </motion.h2>

        <motion.p
          className="text-xs sm:text-sm md:text-base text-foreground/50 tracking-wider uppercase"
          initial={{ opacity: 0, y: 15 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.5, delay: 0.35 }}
        >
          {scene.age} &mdash; {scene.location}
        </motion.p>
      </div>
    </div>
  );
}
