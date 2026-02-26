"""Kling 3.0 video generation via fal.ai API."""

import os
import time

import fal_client
import requests
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("FAL_KEY"):
    raise RuntimeError(
        "FAL_KEY is not set. "
        "Add it to your .env file or export it as an environment variable."
    )

# fal_client reads FAL_KEY from env automatically
MODEL = "fal-ai/kling-video/v3/standard/image-to-video"


def _on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(f"    [kling] {log['message']}")


def generate_video(
    image_path: str,
    prompt: str,
    duration: str = "5",
    aspect_ratio: str = "16:9",
    output_path: str = "output/videos/out.mp4",
) -> str:
    """Generate a video from an image using Kling 3.0.

    Args:
        image_path: Local path to the source image.
        prompt: Motion/camera description for the video.
        duration: Video duration in seconds (as string), 3-15.
        aspect_ratio: Output aspect ratio ("16:9", "9:16", "1:1").
        output_path: Where to save the output MP4.

    Returns:
        Path to the saved video file.
    """
    print(f"  Uploading image to fal.ai: {image_path}")
    image_url = fal_client.upload_file(image_path)
    print(f"  Uploaded: {image_url}")

    print(f"  Generating video (duration={duration}s)...")
    print(f"  Prompt: {prompt[:100]}...")

    start = time.time()
    result = fal_client.subscribe(
        MODEL,
        arguments={
            "start_image_url": image_url,
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
            "generate_audio": True,
            "negative_prompt": "blur, distort, low quality, deformed face, extra limbs",
        },
        with_logs=True,
        on_queue_update=_on_queue_update,
    )
    elapsed = time.time() - start
    print(f"  Video generated in {elapsed:.1f}s")

    video_url = result["video"]["url"]
    print(f"  Downloading video from: {video_url}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    resp = requests.get(video_url, timeout=120)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)

    size_mb = len(resp.content) / (1024 * 1024)
    print(f"  Saved video: {output_path} ({size_mb:.1f} MB)")
    return output_path


if __name__ == "__main__":
    # Quick test — requires an image at output/images/test_prompt.png
    generate_video(
        image_path="output/images/test_prompt.png",
        prompt="Slow camera orbit around the subject, cinematic movement, gentle wind in hair",
        output_path="output/videos/test_video.mp4",
    )
    print("Done!")
