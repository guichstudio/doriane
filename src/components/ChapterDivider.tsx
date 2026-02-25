"use client";

import { motion } from "framer-motion";
import type { Era } from "@/lib/scenes";

export default function ChapterDivider({ era }: { era: Era }) {
  const isFriends = era.id === "friends";
  const lineClass = isFriends ? "bg-purple/30" : "bg-pink/30";
  const subtitleClass = isFriends ? "text-purple" : "text-pink";

  return (
    <div className="h-screen-safe w-full flex items-center justify-center snap-start bg-background px-6">
      <motion.div
        className="text-center"
        initial={{ opacity: 0, scale: 0.95 }}
        whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true, amount: 0.5 }}
        transition={{ duration: 0.8 }}
      >
        {/* Top line */}
        <motion.div
          className={`mx-auto mb-6 sm:mb-8 h-px ${lineClass}`}
          initial={{ width: 0 }}
          whileInView={{ width: 80 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        />

        <h2 className="text-2xl sm:text-4xl md:text-5xl tracking-[0.2em] sm:tracking-[0.25em] uppercase text-foreground/90 font-light mb-3 sm:mb-4">
          {era.label}
        </h2>

        <p className={`text-base sm:text-lg tracking-widest ${subtitleClass} mb-1.5 sm:mb-2`}>{era.subtitle}</p>

        <p className="text-xs sm:text-sm text-foreground/30 tracking-wider">{era.ageRange}</p>

        {/* Bottom line */}
        <motion.div
          className={`mx-auto mt-6 sm:mt-8 h-px ${lineClass}`}
          initial={{ width: 0 }}
          whileInView={{ width: 80 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.5 }}
        />
      </motion.div>
    </div>
  );
}
