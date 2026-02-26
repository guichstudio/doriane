"""FLUX 2.0 PRO image generation via OpenRouter API."""

import base64
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set. "
        "Add it to your .env file or export it as an environment variable."
    )

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "black-forest-labs/flux.2-pro"


def _headers():
    return {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }


def _save_image(response_json: dict, output_path: str) -> str:
    """Extract base64 image from API response and save as PNG."""
    choices = response_json.get("choices", [])
    if not choices:
        raise RuntimeError(f"No choices in response: {response_json}")

    message = choices[0].get("message", {})
    images = message.get("images", [])
    if not images:
        raise RuntimeError(f"No images in response: {response_json}")

    data_url = images[0]["image_url"]["url"]
    _, b64_data = data_url.split(",", 1)
    image_bytes = base64.b64decode(b64_data)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(image_bytes)

    print(f"  Saved image: {output_path}")
    return output_path


def generate_from_prompt(prompt: str, aspect_ratio: str = "16:9", output_path: str = "output/images/out.png") -> str:
    """Generate an image from a text prompt (text-to-image)."""
    print(f"  Generating image from prompt...")
    print(f"  Prompt: {prompt[:100]}...")

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "modalities": ["image"],
        "image_config": {"aspect_ratio": aspect_ratio},
    }

    start = time.time()
    response = requests.post(API_URL, headers=_headers(), json=payload, timeout=120)
    if not response.ok:
        print(f"  API error {response.status_code}: {response.text}")
        response.raise_for_status()
    elapsed = time.time() - start
    print(f"  API responded in {elapsed:.1f}s")

    return _save_image(response.json(), output_path)


def generate_from_image(image_path: str, prompt: str, aspect_ratio: str = "16:9", output_path: str = "output/images/out.png") -> str:
    """Generate an image from a source image + prompt (image-to-image)."""
    print(f"  Generating image from source: {image_path}")
    print(f"  Prompt: {prompt[:100]}...")

    # Encode source image as base64 data URL
    ext = os.path.splitext(image_path)[1].lower()
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}.get(ext.lstrip("."), "image/jpeg")

    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    data_url = f"data:{mime};base64,{b64}"

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            }
        ],
        "modalities": ["image"],
        "image_config": {"aspect_ratio": aspect_ratio},
    }

    start = time.time()
    response = requests.post(API_URL, headers=_headers(), json=payload, timeout=180)
    if not response.ok:
        print(f"  API error {response.status_code}: {response.text}")
        response.raise_for_status()
    elapsed = time.time() - start
    print(f"  API responded in {elapsed:.1f}s")

    return _save_image(response.json(), output_path)


if __name__ == "__main__":
    # Quick test
    generate_from_prompt(
        "A young woman standing in front of the Eiffel Tower, GTA V art style, vibrant colors, dramatic lighting",
        output_path="output/images/test_prompt.png",
    )
    print("Done!")
