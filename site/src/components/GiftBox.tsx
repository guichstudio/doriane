"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import Particle, { type ParticleData } from "./Particle";

type GiftState = "idle" | "opening" | "revealed";

export default function GiftBox() {
  const [giftState, setGiftState] = useState<GiftState>("idle");
  const [particles, setParticles] = useState<ParticleData[]>([]);
  const [burstParticles, setBurstParticles] = useState<ParticleData[]>([]);

  useEffect(() => {
    setParticles(
      Array.from({ length: 15 }, () => ({
        left: `${Math.random() * 100}%`,
        width: `${2 + Math.random() * 3}px`,
        height: `${2 + Math.random() * 3}px`,
        duration: 6 + Math.random() * 4,
      }))
    );
  }, []);

  const handleClick = () => {
    if (giftState !== "idle") return;
    setGiftState("opening");

    setBurstParticles(
      Array.from({ length: 12 }, () => ({
        left: `${30 + Math.random() * 40}%`,
        width: `${3 + Math.random() * 4}px`,
        height: `${3 + Math.random() * 4}px`,
        duration: 2 + Math.random() * 2,
      }))
    );

    setTimeout(() => setGiftState("revealed"), 1200);
  };

  return (
    <div className="relative h-screen-safe w-full flex items-center justify-center snap-start bg-background overflow-hidden">
      {/* Background particles */}
      {particles.map((p, i) => (
        <Particle key={i} data={p} delay={i * 0.4} direction="up" className="bg-purple/20" />
      ))}

      {/* Burst particles on open */}
      {giftState !== "idle" &&
        burstParticles.map((p, i) => (
          <Particle key={`burst-${i}`} data={p} delay={i * 0.05} direction="up" className="bg-purple/40" />
        ))}

      <div className="relative z-10 flex flex-col items-center">
        {/* Title */}
        <motion.p
          className="text-base sm:text-lg text-purple/80 italic mb-8 sm:mb-10 tracking-wide"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          Un cadeau pour toi...
        </motion.p>

        {/* Gift Box */}
        <AnimatePresence>
          {giftState !== "revealed" && (
            <motion.button
              onClick={handleClick}
              className="relative cursor-pointer focus:outline-none"
              aria-label="Ouvrir le cadeau"
              exit={{ scale: 0.3, opacity: 0, y: -80 }}
              transition={{ duration: 0.5, ease: "easeIn" }}
            >
              <motion.div
                animate={giftState === "idle" ? { y: [0, -10, 0] } : { y: 0 }}
                transition={
                  giftState === "idle"
                    ? { repeat: Infinity, duration: 3, ease: "easeInOut" }
                    : { duration: 0.3 }
                }
              >
                {/* Lid */}
                <motion.div
                  className="relative z-10"
                  animate={
                    giftState === "opening"
                      ? { y: -60, rotateZ: -15, opacity: 0 }
                      : { y: 0, rotateZ: 0, opacity: 1 }
                  }
                  transition={{ duration: 0.6, ease: [0.34, 1.56, 0.64, 1] }}
                >
                  {/* Lid top face */}
                  <div
                    className="w-[170px] h-[30px] sm:w-[220px] sm:h-[36px] rounded-t-md border border-purple/40 relative"
                    style={{
                      background: "linear-gradient(135deg, rgba(155,89,182,0.35) 0%, rgba(155,89,182,0.2) 100%)",
                      boxShadow: "0 -4px 20px rgba(155,89,182,0.2)",
                    }}
                  >
                    {/* Lid ribbon horizontal */}
                    <div className="absolute inset-y-0 left-1/2 -translate-x-1/2 w-[22px] sm:w-[28px] bg-purple/50 border-x border-purple/60" />
                    {/* Bow */}
                    <div className="absolute -top-3 left-1/2 -translate-x-1/2 flex gap-0.5">
                      <div className="w-3 h-3 sm:w-4 sm:h-4 rounded-full bg-purple/60 border border-purple/70" />
                      <div className="w-3 h-3 sm:w-4 sm:h-4 rounded-full bg-purple/60 border border-purple/70" />
                    </div>
                  </div>
                </motion.div>

                {/* Box body */}
                <div
                  className="w-[160px] h-[130px] sm:w-[200px] sm:h-[160px] mx-auto rounded-b-md border border-purple/30 relative overflow-hidden"
                  style={{
                    background: "linear-gradient(180deg, rgba(155,89,182,0.25) 0%, rgba(155,89,182,0.12) 100%)",
                    boxShadow: "0 0 40px rgba(155,89,182,0.15), 0 8px 30px rgba(0,0,0,0.3)",
                  }}
                >
                  {/* Ribbon vertical */}
                  <div className="absolute inset-y-0 left-1/2 -translate-x-1/2 w-[22px] sm:w-[28px] bg-purple/40 border-x border-purple/50" />
                  {/* Ribbon horizontal */}
                  <div className="absolute inset-x-0 top-1/2 -translate-y-1/2 h-[22px] sm:h-[28px] bg-purple/40 border-y border-purple/50" />

                  {/* Inner glow */}
                  <AnimatePresence>
                    {giftState === "opening" && (
                      <motion.div
                        className="absolute inset-0"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        style={{
                          background: "radial-gradient(circle at center, rgba(155,89,182,0.6) 0%, transparent 70%)",
                        }}
                      />
                    )}
                  </AnimatePresence>
                </div>

                {/* Glow effect underneath */}
                <motion.div
                  className="absolute -bottom-4 left-1/2 -translate-x-1/2 w-[80%] h-8 rounded-full blur-xl"
                  style={{ background: "rgba(155,89,182,0.2)" }}
                  animate={{ opacity: [0.3, 0.6, 0.3] }}
                  transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
                />
              </motion.div>
            </motion.button>
          )}
        </AnimatePresence>

        {/* Click prompt */}
        <AnimatePresence>
          {giftState === "idle" && (
            <motion.p
              className="mt-6 sm:mt-8 text-sm sm:text-base text-purple/60 tracking-widest uppercase"
              initial={{ opacity: 0 }}
              animate={{ opacity: [0.4, 0.8, 0.4] }}
              exit={{ opacity: 0 }}
              transition={{ repeat: Infinity, duration: 2, ease: "easeInOut" }}
            >
              Appuie pour ouvrir
            </motion.p>
          )}
        </AnimatePresence>

        {/* Revealed content */}
        <AnimatePresence>
          {giftState === "revealed" && (
            <motion.div
              className="text-center px-6 max-w-md mx-auto"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.3 }}
            >
              <motion.div
                className="text-6xl sm:text-7xl mb-5"
                initial={{ opacity: 0, scale: 0.3 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, ease: "backOut" }}
              >
                📸
              </motion.div>

              <motion.h3
                className="gta-title-purple text-3xl sm:text-5xl mb-4"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3, duration: 0.5 }}
              >
                Sony A7III
              </motion.h3>

              <motion.div
                className="mb-6"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6, duration: 0.5 }}
              >
                <p className="text-foreground/40 line-through text-sm sm:text-base mb-1">1 998 &euro;</p>
                <motion.p
                  className="text-4xl sm:text-5xl font-extrabold text-purple"
                  initial={{ scale: 0.8 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: 0.8, duration: 0.4, ease: "backOut" }}
                >
                  &minus;600 &euro;
                </motion.p>
              </motion.div>

              <motion.div
                className="mx-auto h-px bg-purple/30 mb-6"
                initial={{ width: 0 }}
                animate={{ width: 80 }}
                transition={{ delay: 1.0, duration: 0.6 }}
              />

              <motion.p
                className="text-base sm:text-lg text-foreground/70 italic"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1.2, duration: 0.6 }}
              >
                De la part de tous tes amis &hearts;
              </motion.p>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
