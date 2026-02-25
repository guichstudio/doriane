"use client";

import { useRef, useState } from "react";
import { motion } from "framer-motion";

export default function IntroVideo({ onEnd }: { onEnd: () => void }) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [fading, setFading] = useState(false);

  const handleEnded = () => {
    setFading(true);
    setTimeout(onEnd, 800);
  };

  return (
    <motion.div
      className="fixed inset-0 z-50 bg-black flex items-center justify-center"
      initial={{ opacity: 0 }}
      animate={{ opacity: fading ? 0 : 1 }}
      transition={{ duration: 0.8 }}
    >
      <video
        ref={videoRef}
        src="/media/introvideo.mp4"
        autoPlay
        playsInline
        className="w-full h-full object-cover"
        onEnded={handleEnded}
      />

      {/* Skip button */}
      <motion.button
        onClick={handleEnded}
        className="absolute bottom-8 right-8 px-6 py-2 border border-white/20 rounded-full
                   text-white/50 text-xs tracking-[0.15em] uppercase
                   hover:text-white/80 hover:border-white/40 transition-all cursor-pointer"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 2, duration: 0.5 }}
      >
        Passer
      </motion.button>
    </motion.div>
  );
}
