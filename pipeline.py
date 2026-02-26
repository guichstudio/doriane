"""Pipeline to generate GTA-style images and videos for Doriane's journey."""

import argparse
import os
import sys

from dotenv import load_dotenv

load_dotenv()

from generate_image import generate_from_prompt, generate_from_image
from generate_video import generate_video
from scenes import SCENES


def run_scene(name: str, scene: dict, only_images: bool = False, only_videos: bool = False):
    """Run image and/or video generation for a single scene."""
    print(f"\n{'='*60}")
    print(f"  Scene: {scene['name']} ({name})")
    print(f"{'='*60}")

    image_path = f"output/images/{name}.png"
    video_path = f"output/videos/{name}.mp4"

    # --- Image generation ---
    if not only_videos:
        if os.path.exists(image_path):
            print(f"  Image already exists: {image_path} (skipping)")
        else:
            if scene["type"] == "text-to-image":
                generate_from_prompt(
                    prompt=scene["image_prompt"],
                    aspect_ratio=scene["aspect_ratio"],
                    output_path=image_path,
                )
            elif scene["type"] == "image-to-image":
                source = scene["source_image"]
                if not source or not os.path.exists(source):
                    print(f"  ERROR: Source image not found: {source}")
                    return
                generate_from_image(
                    image_path=source,
                    prompt=scene["image_prompt"],
                    aspect_ratio=scene["aspect_ratio"],
                    output_path=image_path,
                )

    # --- Video generation ---
    if not only_images:
        if not os.path.exists(image_path):
            print(f"  ERROR: Image not found for video: {image_path}")
            return
        if os.path.exists(video_path):
            print(f"  Video already exists: {video_path} (skipping)")
        else:
            generate_video(
                image_path=image_path,
                prompt=scene["video_prompt"],
                duration=scene["duration"],
                aspect_ratio=scene["aspect_ratio"],
                output_path=video_path,
            )


def estimate_costs(scene_names: list[str]):
    """Print estimated costs for the selected scenes."""
    n = len(scene_names)
    image_cost = n * 0.03
    video_cost = n * 1.26  # 5s, audio on
    print(f"\nCost estimate for {n} scene(s):")
    print(f"  Images (FLUX 2.0 PRO): {n} x $0.03 = ${image_cost:.2f}")
    print(f"  Videos (Kling 3.0 5s): {n} x $1.26 = ${video_cost:.2f}")
    print(f"  Total: ${image_cost + video_cost:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Doriane's GTA Journey Pipeline")
    parser.add_argument("--scene", type=str, help="Run a single scene by name")
    parser.add_argument("--only-images", action="store_true", help="Only generate images")
    parser.add_argument("--only-videos", action="store_true", help="Only generate videos (images must exist)")
    parser.add_argument("--estimate", action="store_true", help="Show cost estimate and exit")
    parser.add_argument("--list", action="store_true", help="List all available scenes")
    args = parser.parse_args()

    if args.list:
        for i, (key, scene) in enumerate(SCENES.items(), 1):
            print(f"  {i:2d}. {key:<35s} — {scene['name']}")
        return

    if args.scene:
        if args.scene not in SCENES:
            print(f"Unknown scene: {args.scene}")
            print(f"Available: {', '.join(SCENES.keys())}")
            sys.exit(1)
        scene_names = [args.scene]
    else:
        scene_names = list(SCENES.keys())

    if args.estimate:
        estimate_costs(scene_names)
        return

    for name in scene_names:
        run_scene(name, SCENES[name], only_images=args.only_images, only_videos=args.only_videos)

    print(f"\nDone! Processed {len(scene_names)} scene(s).")


if __name__ == "__main__":
    main()
