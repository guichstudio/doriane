"use client";

import { motion } from "framer-motion";

export interface ParticleData {
  left: string;
  width: string;
  height: string;
  duration: number;
}

interface ParticleProps {
  data: ParticleData;
  delay: number;
  direction?: "up" | "down";
  className?: string;
}

export default function Particle({
  data,
  delay,
  direction = "up",
  className = "bg-pink/20",
}: ParticleProps) {
  const isUp = direction === "up";
  const startProp = isUp ? "bottom" : "top";

  return (
    <motion.div
      className={`absolute rounded-full ${className}`}
      style={{ left: data.left, width: data.width, height: data.height }}
      initial={{ [startProp]: "-5%", opacity: 0 }}
      animate={{ [startProp]: "105%", opacity: [0, isUp ? 0.4 : 0.6, 0] }}
      transition={{
        duration: data.duration,
        delay,
        repeat: Infinity,
        ease: "linear",
      }}
    />
  );
}
