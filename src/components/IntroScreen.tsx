"use client";

import { motion } from "framer-motion";
import { useState, useEffect } from "react";

interface ParticleData {
  left: string;
  width: string;
  height: string;
  duration: number;
}

function Particle({ data, index }: { data: ParticleData; index: number }) {
  return (
    <motion.div
      className="absolute rounded-full bg-pink/20"
      style={{ left: data.left, width: data.width, height: data.height }}
      initial={{ bottom: "-5%", opacity: 0 }}
      animate={{ bottom: "105%", opacity: [0, 0.4, 0] }}
      transition={{
        duration: data.duration,
        delay: index * 0.2,
        repeat: Infinity,
        ease: "linear",
      }}
    />
  );
}

export default function IntroScreen({ onEnter }: { onEnter: () => void }) {
  const [particles, setParticles] = useState<ParticleData[]>([]);

  useEffect(() => {
    setParticles(
      Array.from({ length: 25 }, () => ({
        left: `${Math.random() * 100}%`,
        width: `${2 + Math.random() * 2}px`,
        height: `${2 + Math.random() * 2}px`,
        duration: 8 + Math.random() * 6,
      }))
    );
  }, []);

  return (
    <motion.div
      className="fixed inset-0 z-50 flex items-center justify-center bg-background overflow-hidden"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.8 }}
    >
      {/* Particles */}
      {particles.map((p, i) => (
        <Particle key={i} data={p} index={i} />
      ))}

      {/* Content */}
      <div className="relative z-10 text-center px-6 w-full max-w-lg mx-auto">
        <motion.p
          className="text-xs sm:text-sm md:text-base tracking-[0.3em] uppercase text-foreground/40 mb-4 sm:mb-6"
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.6 }}
        >
          un cadeau pour
        </motion.p>

        <motion.h1
          className="gta-title text-6xl sm:text-8xl md:text-9xl mb-3 sm:mb-4"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 1.2 }}
        >
          Doriane
        </motion.h1>

        <motion.p
          className="text-lg sm:text-xl md:text-2xl italic text-pink/70 mb-1.5 sm:mb-2"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 1.6 }}
        >
          Chapter One
        </motion.p>

        <motion.p
          className="text-xs sm:text-sm tracking-[0.2em] uppercase text-foreground/30 mb-8 sm:mb-10"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5, delay: 1.9 }}
        >
          5 ans &mdash; 30 ans
        </motion.p>

        {/* Decorative line */}
        <motion.div
          className="mx-auto h-px bg-pink/30 mb-8 sm:mb-10"
          initial={{ width: 0 }}
          animate={{ width: 120 }}
          transition={{ duration: 0.6, delay: 2.2 }}
        />

        {/* CTA — larger touch target on mobile */}
        <motion.button
          onClick={onEnter}
          className="px-10 py-4 sm:py-3 border border-pink/40 rounded-full text-pink tracking-[0.15em] uppercase text-sm
                     hover:bg-pink/10 hover:shadow-[0_0_30px_rgba(231,76,139,0.2)] active:bg-pink/15
                     transition-all duration-300 cursor-pointer min-w-[160px]"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 2.6 }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          Ouvrir
        </motion.button>
      </div>
    </motion.div>
  );
}
