"use client";

import { motion } from "framer-motion";
import { useState, useEffect } from "react";

interface ParticleData {
  left: string;
  width: string;
  height: string;
  duration: number;
}

function Particle({ data, delay }: { data: ParticleData; delay: number }) {
  return (
    <motion.div
      className="absolute rounded-full bg-pink/30"
      style={{ left: data.left, width: data.width, height: data.height }}
      initial={{ top: "-5%", opacity: 0 }}
      animate={{ top: "105%", opacity: [0, 0.6, 0] }}
      transition={{
        duration: data.duration,
        delay,
        repeat: Infinity,
        ease: "linear",
      }}
    />
  );
}

export default function Finale() {
  const [particles, setParticles] = useState<ParticleData[]>([]);

  useEffect(() => {
    setParticles(
      Array.from({ length: 20 }, () => ({
        left: `${Math.random() * 100}%`,
        width: `${2 + Math.random() * 3}px`,
        height: `${2 + Math.random() * 3}px`,
        duration: 6 + Math.random() * 4,
      }))
    );
  }, []);

  return (
    <div className="relative h-screen-safe w-full flex items-center justify-center snap-start bg-background overflow-hidden">
      {/* Falling particles */}
      {particles.map((p, i) => (
        <Particle key={i} data={p} delay={i * 0.3} />
      ))}

      <div className="relative z-10 text-center px-6 w-full max-w-lg mx-auto">
        <motion.p
          className="text-base sm:text-lg md:text-xl italic text-pink/80 mb-3 sm:mb-4"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          Chapter One
        </motion.p>

        <motion.h2
          className="gta-title text-4xl sm:text-6xl md:text-8xl mb-4 sm:mb-6"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.8 }}
        >
          Joyeux Anniversaire
        </motion.h2>

        <motion.p
          className="text-2xl sm:text-3xl md:text-4xl text-foreground/80 font-light mb-8 sm:mb-10"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7, delay: 1.3 }}
        >
          Doriane
        </motion.p>

        <motion.div
          className="flex justify-center mb-6 sm:mb-8"
          initial={{ opacity: 0, scale: 0 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 1.8 }}
        >
          <span className="text-pink text-2xl sm:text-3xl">&hearts;</span>
        </motion.div>

        <motion.p
          className="text-xs sm:text-sm md:text-base text-foreground/40 tracking-wide max-w-xs sm:max-w-md mx-auto"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 2.3 }}
        >
          30 ans d&apos;aventures. Et ce n&apos;est que le d&eacute;but.
        </motion.p>
      </div>
    </div>
  );
}
