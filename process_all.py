"""Generate manifest.json and copy media files for the website."""

import json
import shutil
from pathlib import Path

from scenes import SCENES

ROOT = Path(__file__).parent
OUTPUT_DIR = ROOT / "output"
SITE_MEDIA = ROOT / "site" / "public" / "media"
MANIFEST_PATH = ROOT / "site" / "public" / "manifest.json"

# Age and location metadata for each scene (shown on the site)
SCENE_META = {
    "scene_01_martinique_childhood": {"age": "5 ans", "location": "Martinique"},
    "scene_02_martinique_carnival": {"age": "7 ans", "location": "Martinique"},
    "scene_03_martinique_garden": {"age": "10 ans", "location": "Martinique"},
    "scene_04_limoges_winter": {"age": "15 ans", "location": "Limoges, France"},
    "scene_05_paris_cozy": {"age": "16 ans", "location": "Paris, France"},
    "scene_06_paris_night": {"age": "18 ans", "location": "Paris, France"},
    "scene_07_nyc_mets": {"age": "25 ans", "location": "NYC, USA"},
    "scene_08_nyc_sunset": {"age": "25 ans", "location": "NYC, USA"},
    "scene_09_dubai_desert": {"age": "26 ans", "location": "Dubai, UAE"},
    "scene_10_sicily_cefalu": {"age": "26 ans", "location": "Cefalù, Sicily"},
    "scene_11_miami_beach": {"age": "27 ans", "location": "Miami, USA"},
    "scene_12_los_angeles": {"age": "27 ans", "location": "Los Angeles, USA"},
    "scene_13_yosemite": {"age": "27 ans", "location": "Yosemite, USA"},
    "scene_14_monument_valley": {"age": "27 ans", "location": "Monument Valley, USA"},
    "scene_15_hawaii": {"age": "28 ans", "location": "Hawaii, USA"},
    "scene_16_bali": {"age": "28 ans", "location": "Bali, Indonesia"},
    "scene_17_singapore": {"age": "29 ans", "location": "Singapore"},
    "scene_18_tokyo_disney": {"age": "30 ans", "location": "Tokyo Disneyland, Japan"},
    "scene_19_waterfall": {"age": "26 ans", "location": "Cascade Tropicale"},
    "scene_20_bryce_canyon": {"age": "27 ans", "location": "Bryce Canyon, USA"},
    "scene_21_nyc_times_square": {"age": "25 ans", "location": "Times Square, NYC"},
    "scene_22_gorge_swim": {"age": "27 ans", "location": "Gorges, France"},
    "scene_23_theme_park": {"age": "27 ans", "location": "Orlando, USA"},
    "scene_24_golden_gate": {"age": "27 ans", "location": "San Francisco"},
    "scene_25_grand_canyon": {"age": "27 ans", "location": "Grand Canyon, USA"},
    "scene_28_fete_foraine": {"age": "18 ans", "location": "Les Issambres, France"},
    "scene_29_chicago_river": {"age": "27 ans", "location": "Chicago, USA"},
    "scene_30_princesses": {"age": "27 ans", "location": "Bridgerton Experience"},
    "scene_31_rooftop_night": {"age": "25 ans", "location": "NYC, USA"},
    "scene_32_monument_valley_duo": {"age": "27 ans", "location": "Monument Valley, USA"},
}


def build_manifest():
    SITE_MEDIA.mkdir(parents=True, exist_ok=True)

    memories = []
    for key, scene in SCENES.items():
        image_path = OUTPUT_DIR / "images" / f"{key}.png"
        if not image_path.exists():
            continue

        # Copy image
        dest_image = SITE_MEDIA / f"{key}.png"
        shutil.copy2(image_path, dest_image)

        meta = SCENE_META.get(key, {})
        entry = {
            "id": key,
            "name": scene["name"],
            "age": meta.get("age", ""),
            "location": meta.get("location", ""),
            "media": [{"type": "image", "src": f"/media/{key}.png"}],
        }

        # Copy video if it exists
        video_path = OUTPUT_DIR / "videos" / f"{key}.mp4"
        if video_path.exists():
            dest_video = SITE_MEDIA / f"{key}.mp4"
            shutil.copy2(video_path, dest_video)
            entry["media"].append({"type": "video", "src": f"/media/{key}.mp4"})

        memories.append(entry)
        print(f"  {scene['name']} ({meta.get('age', '?')}) — {len(entry['media'])} file(s)")

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(memories, indent=2, ensure_ascii=False))
    print(f"\n  {len(memories)} scenes written to {MANIFEST_PATH}")


if __name__ == "__main__":
    build_manifest()
