"use client";

import { SCENES } from "@/lib/scenes";

export default function Timeline({ activeIndex }: { activeIndex: number }) {
  const handleClick = (id: string) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="fixed left-6 top-1/2 -translate-y-1/2 z-40 hidden md:flex flex-col items-center gap-0">
      {/* Vertical line behind dots */}
      <div className="absolute inset-0 flex justify-center pointer-events-none">
        <div className="w-px h-full bg-foreground/10" />
      </div>

      {SCENES.map((scene, i) => {
        const isActive = i === activeIndex;
        const isPast = i < activeIndex;
        const isFriends = scene.era === "friends";

        return (
          <button
            key={scene.id}
            onClick={() => handleClick(scene.id)}
            title={scene.name}
            className="relative z-10 p-1.5 group cursor-pointer"
          >
            <div
              className={`rounded-full transition-all duration-300 ${
                isActive
                  ? isFriends
                    ? "w-2.5 h-2.5 bg-purple shadow-[0_0_10px_rgba(155,89,182,0.6)]"
                    : "w-2.5 h-2.5 bg-pink shadow-[0_0_10px_rgba(231,76,139,0.6)]"
                  : isPast
                  ? isFriends
                    ? "w-1.5 h-1.5 bg-purple/60"
                    : "w-1.5 h-1.5 bg-pink/60"
                  : "w-1.5 h-1.5 bg-foreground/20"
              }`}
            />

            {/* Tooltip */}
            <span className="absolute left-8 top-1/2 -translate-y-1/2 whitespace-nowrap text-xs text-foreground/60 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
              {scene.name}
            </span>
          </button>
        );
      })}
    </div>
  );
}
