"use client";

import { motion } from "framer-motion";
import { useState, useRef, useCallback, useEffect } from "react";
import { LOCATIONS, type Location } from "@/lib/locations";
import { SCENES } from "@/lib/scenes";

interface WorldMapProps {
  onSelectScene: (sceneIndex: number) => void;
  onStart: () => void;
}

// SVG aspect ratio from viewBox: 784.077 / 458.627
const SVG_ASPECT = 784.077 / 458.627; // ≈ 1.7096

const MIN_ZOOM = 1;
const MAX_ZOOM = 4;

function MapPin({
  location,
  index,
  onSelect,
  zoom,
}: {
  location: Location;
  index: number;
  onSelect: (sceneIndex: number) => void;
  zoom: number;
}) {
  const [hovered, setHovered] = useState(false);
  const mainScene = location.scenes[0];
  const sceneIndex = SCENES.findIndex((s) => s.id === mainScene.id);
  const isFriends = location.scenes.every((s) => s.era === "friends");

  // Scale down pins as user zooms in so they don't become huge
  const pinScale = 1 / Math.sqrt(zoom);

  return (
    <motion.div
      className="absolute -translate-x-1/2 -translate-y-1/2 group"
      style={{
        left: `${location.x}%`,
        top: `${location.y}%`,
        scale: pinScale,
      }}
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: pinScale, opacity: 1 }}
      transition={{ delay: 0.8 + index * 0.08, duration: 0.4, type: "spring" }}
    >
      {/* Clickable pin area */}
      <motion.button
        className="relative cursor-pointer"
        onClick={(e) => {
          e.stopPropagation();
          onSelect(sceneIndex);
        }}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        onTouchStart={() => setHovered(true)}
        onTouchEnd={() => setHovered(false)}
        whileHover={{ scale: 1.3, zIndex: 50 }}
        whileTap={{ scale: 0.95 }}
      >
        {/* Main thumbnail */}
        {location.scenes.length === 1 ? (
          <div className={`w-11 h-11 sm:w-13 sm:h-13 rounded-full overflow-hidden border-2 ${
            isFriends
              ? "border-purple/60 shadow-[0_0_12px_rgba(155,89,182,0.4)]"
              : "border-pink/60 shadow-[0_0_12px_rgba(231,76,139,0.4)]"
          }`}>
            <img
              src={mainScene.image}
              alt={mainScene.name}
              className="w-full h-full object-cover"
              draggable={false}
            />
          </div>
        ) : (
          /* Multi-scene cluster */
          <div className="relative w-14 h-14 sm:w-16 sm:h-16">
            {location.scenes.map((scene, i) => {
              const angle =
                ((i - (location.scenes.length - 1) / 2) * 25 * Math.PI) / 180;
              const offsetX = Math.sin(angle) * 10;
              const offsetY = -Math.cos(angle) * 6;
              return (
                <div
                  key={scene.id}
                  className={`absolute top-1/2 left-1/2 w-9 h-9 sm:w-10 sm:h-10 -translate-x-1/2 -translate-y-1/2 rounded-full overflow-hidden border-2 ${
                    isFriends
                      ? "border-purple/60 shadow-[0_0_10px_rgba(155,89,182,0.3)]"
                      : "border-pink/60 shadow-[0_0_10px_rgba(231,76,139,0.3)]"
                  }`}
                  style={{
                    transform: `translate(calc(-50% + ${offsetX}px), calc(-50% + ${offsetY}px))`,
                    zIndex: location.scenes.length - i,
                  }}
                >
                  <img
                    src={scene.image}
                    alt={scene.name}
                    className="w-full h-full object-cover"
                    draggable={false}
                  />
                </div>
              );
            })}
          </div>
        )}
      </motion.button>

      {/* Tooltip */}
      <motion.div
        className="absolute left-1/2 -translate-x-1/2 bottom-full mb-2 pointer-events-none whitespace-nowrap"
        initial={false}
        animate={{ opacity: hovered ? 1 : 0, y: hovered ? 0 : 4 }}
        transition={{ duration: 0.15 }}
      >
        <div className={`bg-black/80 backdrop-blur-sm border ${isFriends ? "border-purple/30" : "border-pink/30"} rounded-lg px-3 py-1.5 text-center`}>
          <p className={`${isFriends ? "text-purple" : "text-pink"} text-xs font-semibold`}>{location.name}</p>
          {location.scenes.length === 1 ? (
            <p className="text-foreground/50 text-[10px]">{mainScene.name}</p>
          ) : (
            <p className="text-foreground/50 text-[10px]">
              {location.scenes.length} souvenirs
            </p>
          )}
        </div>
      </motion.div>
    </motion.div>
  );
}

export default function WorldMap({ onSelectScene, onStart }: WorldMapProps) {
  const [zoom, setZoom] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);
  const dragStart = useRef({ x: 0, y: 0 });
  const panStart = useRef({ x: 0, y: 0 });
  const containerRef = useRef<HTMLDivElement>(null);

  // Clamp pan so map doesn't go off screen
  const clampPan = useCallback(
    (px: number, py: number, z: number) => {
      if (z <= 1) return { x: 0, y: 0 };
      const container = containerRef.current;
      if (!container) return { x: px, y: py };

      const rect = container.getBoundingClientRect();
      const maxPanX = (rect.width * (z - 1)) / 2;
      const maxPanY = (rect.height * (z - 1)) / 2;

      return {
        x: Math.max(-maxPanX, Math.min(maxPanX, px)),
        y: Math.max(-maxPanY, Math.min(maxPanY, py)),
      };
    },
    []
  );

  // Mouse wheel zoom
  const handleWheel = useCallback(
    (e: React.WheelEvent) => {
      e.preventDefault();
      const delta = e.deltaY > 0 ? -0.15 : 0.15;
      setZoom((prev) => {
        const next = Math.max(MIN_ZOOM, Math.min(MAX_ZOOM, prev + delta));
        // Adjust pan when zooming out
        if (next < prev) {
          setPan((p) => clampPan(p.x, p.y, next));
        }
        return next;
      });
    },
    [clampPan]
  );

  // Drag to pan
  const handlePointerDown = useCallback(
    (e: React.PointerEvent) => {
      if (zoom <= 1) return;
      // Only start drag on the map background, not on pins
      setIsDragging(true);
      dragStart.current = { x: e.clientX, y: e.clientY };
      panStart.current = { ...pan };
      (e.target as HTMLElement).setPointerCapture(e.pointerId);
    },
    [zoom, pan]
  );

  const handlePointerMove = useCallback(
    (e: React.PointerEvent) => {
      if (!isDragging) return;
      const dx = e.clientX - dragStart.current.x;
      const dy = e.clientY - dragStart.current.y;
      setPan(clampPan(panStart.current.x + dx, panStart.current.y + dy, zoom));
    },
    [isDragging, zoom, clampPan]
  );

  const handlePointerUp = useCallback(() => {
    setIsDragging(false);
  }, []);

  // Touch pinch-to-zoom
  const lastTouchDist = useRef(0);
  const handleTouchStart = useCallback((e: React.TouchEvent) => {
    if (e.touches.length === 2) {
      const dx = e.touches[0].clientX - e.touches[1].clientX;
      const dy = e.touches[0].clientY - e.touches[1].clientY;
      lastTouchDist.current = Math.sqrt(dx * dx + dy * dy);
    }
  }, []);

  const handleTouchMove = useCallback(
    (e: React.TouchEvent) => {
      if (e.touches.length === 2) {
        e.preventDefault();
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const delta = (dist - lastTouchDist.current) * 0.01;
        lastTouchDist.current = dist;
        setZoom((prev) => {
          const next = Math.max(MIN_ZOOM, Math.min(MAX_ZOOM, prev + delta));
          if (next < prev) {
            setPan((p) => clampPan(p.x, p.y, next));
          }
          return next;
        });
      }
    },
    [clampPan]
  );

  // Reset zoom on double click
  const handleDoubleClick = useCallback(() => {
    if (zoom > 1) {
      setZoom(1);
      setPan({ x: 0, y: 0 });
    } else {
      setZoom(2);
    }
  }, [zoom]);

  return (
    <motion.div
      className="fixed inset-0 z-40 flex flex-col items-center justify-center bg-background overflow-hidden"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.6 }}
    >
      {/* Title */}
      <motion.div
        className="absolute top-0 left-0 right-0 z-20 text-center pt-8 sm:pt-12"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 0.6 }}
      >
        <h2 className="gta-title text-3xl sm:text-5xl md:text-6xl mb-2">
          The World of Doriane
        </h2>
        <p className="text-foreground/30 text-xs sm:text-sm tracking-[0.15em] uppercase">
          24 souvenirs · 21 destinations · 3 continents
        </p>
      </motion.div>

      {/* Map container — outer viewport (clips overflow) */}
      <div
        ref={containerRef}
        className="relative w-full h-full max-w-6xl mx-auto px-4 overflow-hidden select-none"
        onWheel={handleWheel}
        onPointerDown={handlePointerDown}
        onPointerMove={handlePointerMove}
        onPointerUp={handlePointerUp}
        onPointerCancel={handlePointerUp}
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onDoubleClick={handleDoubleClick}
        style={{ cursor: zoom > 1 ? (isDragging ? "grabbing" : "grab") : "default", touchAction: "none" }}
      >
        {/* Inner container: zoom + pan transform, aspect-ratio locked to SVG */}
        <div
          className="absolute inset-0 flex items-center justify-center transition-transform duration-100 ease-out"
          style={{
            transform: `translate(${pan.x}px, ${pan.y}px) scale(${zoom})`,
          }}
        >
          {/* Aspect-ratio-locked map area — pins are positioned relative to this */}
          <div
            className="relative w-full"
            style={{ aspectRatio: `${SVG_ASPECT}`, maxHeight: "100%" }}
          >
            {/* SVG map background */}
            <motion.img
              src="/world-map.svg"
              alt=""
              className="absolute inset-0 w-full h-full pointer-events-none"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1.2, delay: 0.2 }}
              draggable={false}
            />

            {/* Location pins */}
            {LOCATIONS.map((loc, i) => (
              <MapPin
                key={loc.name}
                location={loc}
                index={i}
                onSelect={onSelectScene}
                zoom={zoom}
              />
            ))}
          </div>
        </div>
      </div>

      {/* Zoom controls */}
      <motion.div
        className="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 z-20 flex flex-col gap-2"
        initial={{ opacity: 0, x: 20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ delay: 1.5, duration: 0.4 }}
      >
        <button
          onClick={() => setZoom((z) => Math.min(MAX_ZOOM, z + 0.5))}
          className="w-9 h-9 rounded-full border border-pink/30 bg-black/60 backdrop-blur-sm text-pink flex items-center justify-center hover:bg-pink/10 transition-colors cursor-pointer"
        >
          +
        </button>
        <button
          onClick={() => {
            const next = Math.max(MIN_ZOOM, zoom - 0.5);
            setZoom(next);
            setPan((p) => clampPan(p.x, p.y, next));
          }}
          className="w-9 h-9 rounded-full border border-pink/30 bg-black/60 backdrop-blur-sm text-pink flex items-center justify-center hover:bg-pink/10 transition-colors cursor-pointer"
        >
          −
        </button>
        {zoom > 1 && (
          <button
            onClick={() => {
              setZoom(1);
              setPan({ x: 0, y: 0 });
            }}
            className="w-9 h-9 rounded-full border border-pink/30 bg-black/60 backdrop-blur-sm text-pink flex items-center justify-center hover:bg-pink/10 transition-colors text-[10px] cursor-pointer"
          >
            ↺
          </button>
        )}
      </motion.div>

      {/* Bottom CTA */}
      <motion.div
        className="absolute bottom-0 left-0 right-0 z-20 text-center pb-8 sm:pb-12"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 2, duration: 0.6 }}
      >
        <motion.button
          onClick={onStart}
          className="px-10 py-4 sm:py-3 border border-pink/40 rounded-full text-pink tracking-[0.15em] uppercase text-sm
                     hover:bg-pink/10 hover:shadow-[0_0_30px_rgba(231,76,139,0.2)] active:bg-pink/15
                     transition-all duration-300 cursor-pointer min-w-[200px]"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          Commencer le voyage
        </motion.button>
      </motion.div>
    </motion.div>
  );
}
