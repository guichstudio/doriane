"""Scene definitions for Doriane's GTA-style life journey — 5 to 30 years old."""

# ---------------------------------------------------------------------------
# Character descriptions at different ages
# ---------------------------------------------------------------------------

DORIANE_CHILD_5 = (
    "small young girl around 4-5 years old with big blonde curly hair, "
    "round face, brown eyes, olive-tan skin, wearing a navy blue rain jacket "
    "with white snap buttons"
)

DORIANE_CHILD_8 = (
    "young girl around 7-8 years old with curly blonde-brown hair tied up under "
    "a traditional madras headwrap (orange-red-yellow plaid), brown eyes, "
    "red lipstick, white traditional outfit"
)

DORIANE_CHILD_10 = (
    "girl around 8-10 years old with very long wavy light-brown braided hair "
    "reaching past waist, olive-tan skin, brown eyes, warm smile, "
    "wearing a green spaghetti-strap tank top and pink shorts"
)

DORIANE_TEEN = (
    "slim teenage girl with long dark curly hair, brown eyes, olive-tan skin"
)

DORIANE_ADULT = (
    "slim young woman with long dark brown wavy curly hair, olive-tan skin, "
    "brown eyes, bright warm smile"
)

# ---------------------------------------------------------------------------
# GTA V style prefix — much more aggressive than the original
# ---------------------------------------------------------------------------

STYLE = (
    "Screenshot from a next-gen open-world action-adventure video game, in-game third-person view. "
    "Ultra-high-quality real-time 3D rendering, Unreal Engine 5 level graphics. "
    "Soft cinematic atmospheric haze, volumetric god rays, warm color grading. "
    "Rich vibrant colors, natural golden-hour lighting, soft ambient occlusion, gentle depth of field. "
    "Detailed game textures on surfaces, realistic PBR materials, bloom on light sources. "
    "Atmospheric fog in the distance, painterly soft edges, cinematic mood. "
    "Video game graphics, NOT a photograph. "
)

# ---------------------------------------------------------------------------
# All scenes
# ---------------------------------------------------------------------------

SCENES = {
    # ===== CHILDHOOD — MARTINIQUE (5-10) =====

    "scene_01_martinique_childhood": {
        "name": "Les Premiers Pas",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"A {DORIANE_CHILD_5}, "
            "standing on green grass in front of a small colorful Creole house in Martinique. "
            "Tropical garden with banana trees, hibiscus flowers, a red dirt path. "
            "She looks at the camera with an innocent smile. "
            "Third-person gameplay camera. "
            "Bright tropical morning sun, lush Caribbean vegetation, warm saturated greens."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A small girl with big curly hair starts walking forward along a tropical street in Martinique. "
            "She walks steadily away from camera, never turning back. "
            "Tropical breeze moves the palm trees and flowers around her. "
            "Colorful Creole houses on both sides. Warm golden sunlight. "
            "Camera follows smoothly from behind as she walks. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_02_martinique_carnival": {
        "name": "Carnaval",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"A {DORIANE_CHILD_8}, "
            "standing in a colorful carnival parade in Fort-de-France, Martinique. "
            "Dancers in elaborate costumes behind her, floats decorated with tropical flowers, "
            "confetti in the air, crowds of people along the street. "
            "Bright tropical afternoon sun, vibrant saturated colors everywhere. "
            "Low-angle hero shot, camera looking up at her."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young girl in traditional madras headwrap walks forward through a colorful Caribbean carnival parade. "
            "She walks steadily away from camera, never turning back. "
            "Confetti falls around her, dancers move on both sides, music energy. "
            "Vibrant costumes and floats everywhere. Bright tropical sunlight. "
            "Camera follows smoothly from behind as she walks through the parade. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_03_martinique_garden": {
        "name": "Fleur des Îles",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"A {DORIANE_CHILD_10}, "
            "holding a large white hibiscus flower next to her face, standing in a lush tropical garden. "
            "Thick green foliage everywhere, palm trees, tropical plants, dappled sunlight through leaves. "
            "A small wooden Creole house visible behind the vegetation. "
            "Warm Caribbean afternoon light filtering through the canopy. "
            "Close-up Snapmatic camera perspective, shallow depth of field."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young girl with long braided hair walks forward through a lush tropical garden path. "
            "She walks steadily away from camera, never turning back. "
            "Tropical plants and palm trees on both sides, dappled sunlight through the canopy. "
            "A small Creole house visible ahead. Warm Caribbean light. "
            "Camera follows smoothly from behind as she walks along the garden path. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    # ===== TEEN YEARS — FRANCE (15-18) =====

    "scene_04_limoges_winter": {
        "name": "Hiver à Limoges",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_TEEN}, "
            "wearing a Lakers beanie with yellow pom-pom and a black turtleneck, "
            "walking down a quiet street in a small French town in winter. "
            "Medieval stone buildings, a cathedral in the background, bare trees, "
            "grey overcast sky, a few people with winter coats walking. "
            "Cold winter afternoon light, breath visible in the air. "
            "Third-person gameplay camera following from behind."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A teenage girl in a Lakers beanie walks forward down a quiet French winter street. "
            "She walks steadily away from camera, never turning back, hands in pockets. "
            "Bare tree branches sway in the wind, a few snowflakes falling. "
            "Medieval stone buildings and a cathedral ahead. Cold winter light. "
            "Camera follows smoothly from behind as she walks. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_05_paris_cozy": {
        "name": "Soirées Parisiennes",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_TEEN}, "
            "with long wavy dark brown hair, wearing a soft cream fuzzy sweater, "
            "sitting on a couch in a cozy Parisian apartment. "
            "Warm ambient lamp light, bookshelves, a window showing the Paris rooftops at night, "
            "a cup of tea on the table, fairy lights on the wall. "
            "Warm yellow-orange indoor lighting. "
            "Close-up Snapmatic camera perspective, warm intimate framing."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young woman in a cream sweater walks forward through a cozy Parisian street at dusk. "
            "She walks steadily away from camera, never turning back. "
            "Warm glowing shop windows and cafe terraces on both sides. "
            "Paris rooftops visible, fairy lights and warm amber light everywhere. "
            "Camera follows smoothly from behind as she walks. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_06_paris_night": {
        "name": "Nuits de Paris",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_TEEN}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long straight dark brown hair with bangs, wearing a mauve pink top, "
            "walking away from camera down a cobblestone street in Paris at night. "
            "Warm restaurant light spilling onto the cobblestone street, neon sign above, "
            "other diners visible through the window, wet cobblestones reflecting lights, "
            "the Eiffel Tower glowing faintly in the far background. "
            "Nighttime Parisian scene."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young woman with bangs in a pink top walks FORWARD away from camera down a Parisian cobblestone street at night. "
            "She moves forward steadily, never turning back, walking into the distance. "
            "Warm restaurant lights and neon signs on both sides, wet cobblestones reflecting lights. "
            "The Eiffel Tower glows faintly ahead in the distance. "
            "Camera follows smoothly from behind as she walks forward. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    # ===== ADULT TRAVELS — WORLD (20-30) =====

    "scene_07_nyc_mets": {
        "name": "Game Night",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "with long dark hair in two braids, wearing a Mets #63 pinstripe baseball jersey "
            "over a grey t-shirt. SEEN FROM BEHIND — third-person gameplay camera positioned "
            "several meters behind and slightly above the character, classic GTA V walking perspective. "
            "She is walking through the upper deck at Citi Field baseball stadium. "
            "The massive scoreboard glowing blue ahead of her, crowd in the stands, "
            "the baseball diamond lit by harsh stadium lights below. "
            "Night game atmosphere, stadium lights create harsh pools of light."
        ),
        "video_prompt": (
            "The character walks forward toward the railing at the edge of the upper deck. "
            "She reaches the barrier railing and stops, placing her hands on it. "
            "She stands still looking out at the baseball diamond below, taking in the view. "
            "The crowd cheers, stadium lights flare, the scoreboard glows. "
            "Camera stays behind her the whole time. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_08_nyc_sunset": {
        "name": "Skyline Dorée",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "with shoulder-length wavy dark brown hair, wearing a brown leather jacket "
            "and carrying a leather shoulder bag, standing at a waterfront railing. "
            "Looking back over her shoulder with a smile. "
            "Behind her, the Manhattan skyline at sunset — skyscrapers silhouetted against "
            "a pink and orange sky, the East River reflecting golden light. "
            "Golden hour volumetric lighting, god rays, heavy bloom. "
            "Third-person camera positioned behind and slightly above."
        ),
        "video_prompt": (
            "The character walks forward along the waterfront toward the railing. "
            "She reaches the railing and stops, leaning on it, looking out at the Manhattan skyline. "
            "Wind gently moves her hair. Golden sunset light shifts across the skyscrapers. "
            "Water ripples below, reflecting golden light. "
            "Camera stays behind her the whole time. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_09_dubai_desert": {
        "name": "Sable d'Or",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "with long dark curly hair blowing in the wind, wearing a black crop top, "
            "loose white linen pants, and grey sneakers. "
            "Standing on top of a massive golden sand dune in the Arabian desert, "
            "endless dunes stretching to the horizon. Footprints trailing behind her in the sand. "
            "Late afternoon golden hour, harsh sun, heat haze on distant dunes. "
            "Wide establishing shot, epic desert scale, game engine desert environment textures."
        ),
        "video_prompt": (
            "The character walks forward along the ridge of a golden sand dune in the desert. "
            "She moves steadily forward away from camera, leaving footprints in the sand. "
            "Her hair and pants blow in the desert wind. "
            "Golden sunlight, dust particles floating in the air. Endless dunes ahead. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_10_sicily_cefalu": {
        "name": "Dolce Vita",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with shoulder-length wavy dark brown hair, wearing a black lace camisole top, "
            "white lace mini skirt, white ankle socks and black loafers. "
            "Walking away from camera along a stone pier by the turquoise water. "
            "Ahead of her, the old town of Cefalù with honey-colored buildings, "
            "a dramatic cliff face rising above, swimmers in the water. "
            "Warm Mediterranean late afternoon light."
        ),
        "video_prompt": (
            "The character is far from the edge of the pier, she starts walking slowly forward. "
            "She walks at a slow relaxed pace along the stone pier, taking her time. "
            "Turquoise water on both sides, swimmers splashing gently. "
            "She gradually approaches the edge of the pier over the full 8 seconds. "
            "The honey-colored buildings and cliff of Cefalù ahead. "
            "Warm afternoon sunlight. Camera stays behind her. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_11_miami_beach": {
        "name": "Ocean Drive",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "10",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark wavy hair and sunglasses, wearing a light summer outfit, "
            "walking away from camera along Ocean Drive in Miami Beach. "
            "Art Deco buildings in pastel pink and turquoise, neon signs, palm trees lining the boulevard, "
            "convertible cars parked along the street, rollerbladers, beach visible across the road. "
            "Warm tropical sunset, pink and orange sky, neon glow starting to light up."
        ),
        "video_prompt": (
            "The character walks forward along Ocean Drive in Miami at sunset. "
            "She moves steadily forward away from camera, never turning back. Hair swaying. "
            "Palm trees sway, neon signs flicker on, a convertible drives past. "
            "Art Deco buildings in pastel colors on both sides. Warm tropical sunset light. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_12_los_angeles": {
        "name": "City of Angels",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark wavy hair and sunglasses, wearing a casual chic outfit, "
            "walking away from camera on a hilltop trail overlooking Los Angeles. "
            "The Hollywood sign visible ahead in the distance. "
            "The sprawling city of Los Angeles stretches below, palm trees dotting the landscape, "
            "cars on the highway, the sun setting behind the hills. "
            "Golden California light, heavy god rays."
        ),
        "video_prompt": (
            "The character walks forward along a hilltop trail overlooking Los Angeles. "
            "She moves steadily forward away from camera, never turning back. "
            "The Hollywood sign and sprawling city visible ahead. "
            "Golden California sunset light, god rays through the haze. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_13_yosemite": {
        "name": "Wild & Free",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "with long dark curly hair and a white lace bandana headscarf, "
            "wearing a white crop top, long flowing white button-down skirt, and dark cowboy boots. "
            "Walking across a wooden plank bridge over a stream in a vast green mountain meadow. "
            "Snow-capped mountains and pine forests in the background, bright blue sky with white clouds. "
            "Bright midday sunshine, epic nature scale, bohemian free spirit. "
            "Third-person camera following from behind."
        ),
        "video_prompt": (
            "Subtle movement only — keep the exact same environment and character appearance. "
            "A woman with a backpack and dark jacket stands on a rocky cliff overlooking Yosemite valley. "
            "Gentle wind blows her curly hair. She stays still, taking in the epic view. "
            "Soft clouds drift slowly in the sky. Light shifts subtly. "
            "No changes to clothing, environment, or character. "
            "Camera stays perfectly still behind her."
        ),
    },

    "scene_14_monument_valley": {
        "name": "Red Earth",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark curly hair, wearing a grey crop top and red-white gingham shorts, "
            "walking away from camera along a dirt road through Monument Valley. "
            "The iconic red sandstone buttes rise from the desert floor ahead of her "
            "against a bright blue sky. The road stretches into the distance. "
            "Bright harsh midday light, dramatic American West landscape."
        ),
        "video_prompt": (
            "The character walks forward along a dirt road through Monument Valley. "
            "She wears a grey crop top and gingham shorts, long dark curly hair blowing in the wind. "
            "She moves steadily forward away from camera toward the red sandstone buttes ahead. "
            "Same desert environment throughout, no scene changes. "
            "Bright sunlight, blue sky, red earth. "
            "Camera stays behind her, following her forward motion."
        ),
    },

    "scene_15_hawaii": {
        "name": "Aloha",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark wavy hair with a tropical flower tucked behind her ear, "
            "wearing a flowing tropical dress, walking away from camera on a black volcanic beach. "
            "Turquoise waves crashing on black sand, lush green volcanic cliffs rising ahead, "
            "surfers in the water, a rainbow forming in the mist from the waves. "
            "Late afternoon golden tropical light, dramatic volcanic landscape."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young woman with long dark wavy hair and a tropical flower behind her ear, "
            "wearing a flowing tropical dress, walks forward on a black volcanic beach in Hawaii. "
            "She moves steadily forward away from camera, never turning back. "
            "Turquoise waves crash on the black sand beside her, dress flowing in the breeze. "
            "Green volcanic cliffs ahead, rainbow in the mist. Warm golden tropical light. "
            "Same environment throughout, no scene changes. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_16_bali": {
        "name": "Temple Sacré",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "12",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark wavy hair, wearing a traditional Balinese sarong and white top, "
            "walking away from camera up the stone steps of an ancient temple covered in moss. "
            "Intricate stone carvings and guardian statues flanking the entrance ahead, "
            "tropical jungle surrounding the temple, incense smoke drifting in the humid air, "
            "offerings of flowers on the stone steps. "
            "Soft misty morning light filtering through the jungle canopy."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young woman with long dark wavy hair, wearing a traditional Balinese sarong and white top, "
            "walks forward up the stone steps of an ancient mossy temple. "
            "She moves steadily forward away from camera, never turning back. "
            "Incense smoke swirls around her, mist drifts through the jungle. "
            "Stone carvings and guardian statues on both sides. Soft misty morning light. "
            "Same environment throughout, no scene changes. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_17_singapore": {
        "name": "Néons d'Asie",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark wavy hair, wearing a chic evening outfit, "
            "walking away from camera along a rooftop bar terrace at night. "
            "Ahead of her, the Singapore skyline — Marina Bay Sands illuminated, "
            "Gardens by the Bay supertrees glowing in purple and blue, "
            "futuristic skyscrapers, lights reflecting on the water. "
            "Night scene with neon glow, pink and blue lights, "
            "subtle bloom on neon sources, wet surfaces with mirror reflections."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young woman with long dark wavy hair in a chic evening outfit "
            "walks forward at a normal walking pace along a rooftop bar terrace in Singapore at night. "
            "She moves forward away from camera at regular speed, never turning back. "
            "Marina Bay Sands and the Supertrees glow ahead, neon reflections on wet surfaces. "
            "Pink and blue lights, futuristic skyline. "
            "Same environment throughout, no scene changes. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_18_tokyo_disney": {
        "name": "The Surprise",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"{DORIANE_ADULT}, "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the character, classic GTA V walking perspective. "
            "with long dark wavy hair, both arms raised high in the air in pure joy and celebration, "
            "walking away from camera towards Cinderella's Castle at Tokyo Disneyland lit up in magical colors — "
            "pink, blue, purple lights on the castle. "
            "Fireworks exploding in the sky above the castle, colorful sparkles raining down. "
            "Night scene with spectacular magical lighting, subtle bloom, particle effects."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A young woman with long dark wavy hair, arms raised high in the air in joy, "
            "walks forward toward Cinderella's Castle at Tokyo Disneyland at night. "
            "She moves forward away from camera, joyful and celebrating, arms up. "
            "Fireworks explode in the sky above the castle, colorful sparkles rain down. "
            "Castle lights shift from pink to blue to purple. Magical atmosphere. "
            "Same environment throughout, no scene changes. "
            "Camera stays behind her, following her forward motion. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    # ===== NEW SCENES — IMAGE-TO-IMAGE FROM PHOTOS =====

    "scene_19_waterfall": {
        "name": "Force de la Nature",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            f"SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            f"Two young women with long dark hair, {DORIANE_ADULT} and her friend, "
            "SEEN FROM BEHIND standing on dark volcanic rocks at the base of a massive thundering waterfall, "
            "both with arms raised high in triumph and joy, water drenching them. "
            "The waterfall towers above them, water crashing down creating a huge spray of mist. "
            "Lush tropical vegetation on the cliff edges, dark wet rocks everywhere. "
            "Volumetric god rays piercing through the water spray, subtle bloom on light sources. "
            "Rich vibrant colors, natural lighting, epic scale."
        ),
        "video_prompt": (
            "A GTA V in-game cutscene third-person shot. Two characters seen from behind at the base of a massive waterfall "
            "with arms raised in triumph. The waterfall thunders down, mist swirling everywhere. "
            "Water crashes on the dark rocks, splashing and spraying. "
            "Heavy GTA V film grain throughout — visible noise across the entire frame. "
            "RAGE engine textures, desaturated color grading. "
            "Camera slowly pushes in toward them. "
            "This looks like a GTA V gameplay recording — video game graphics, not photorealistic."
        ),
    },

    "scene_20_bryce_canyon": {
        "name": "Les Trois Explorateurs",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            "Three friends SEEN FROM BEHIND standing at a viewpoint railing overlooking Bryce Canyon — "
            "a young blonde woman in a grey t-shirt on the left, "
            f"a {DORIANE_ADULT} in a white t-shirt in the middle, "
            "and a young man in a navy blue t-shirt with a backwards black cap on the right. "
            "They stand side by side looking out at the spectacular orange-red hoodoo rock formations "
            "stretching to the horizon, green pine trees between the spires, winding trail below. "
            "Overcast sky with dramatic clouds. Metal railing at the viewpoint. "
            "Volumetric god rays, rich vibrant colors, epic landscape scale."
        ),
        "video_prompt": (
            "A GTA V in-game cutscene third-person shot. Three friends seen from behind at a Bryce Canyon viewpoint. "
            "They stand at the railing looking out at the epic orange hoodoo formations. "
            "Gentle wind blows their hair. Clouds drift slowly overhead. "
            "Heavy GTA V film grain throughout — visible noise across the entire frame. "
            "RAGE engine textures, warm desaturated color grading. "
            "Camera stays behind them, very slight drift. "
            "This looks like a GTA V gameplay recording — video game graphics, not photorealistic."
        ),
    },

    "scene_21_nyc_times_square": {
        "name": "NYC Pizza Night",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            "Two young women SEEN FROM BEHIND walking through Times Square at night, each holding a big NYC pizza slice — "
            f"a {DORIANE_ADULT} with long dark hair in a braid wearing a dark jacket on the left, "
            "and her friend with curly afro hair and round glasses wearing a beige coat on the right. "
            "Ahead of them, massive neon billboards glowing in red, yellow, green, "
            "bright LED screens, Broadway signs, crowds of people, yellow taxi cabs on the road. "
            "Nighttime neon glow, subtle bloom on neon sources, rich vibrant neon colors reflecting on wet streets."
        ),
        "video_prompt": (
            "A GTA V in-game cutscene third-person shot. Two young women seen from behind walking through Times Square at night "
            "holding pizza slices. They walk forward steadily away from camera. "
            "Neon signs flash and change colors, crowds walk past, a yellow taxi drives by. "
            "Heavy GTA V film grain throughout — visible noise across the entire frame. "
            "RAGE engine textures, neon nighttime color grading with heavy bloom. "
            "Camera follows smoothly from behind. "
            "This looks like a GTA V gameplay recording — video game graphics, not photorealistic."
        ),
    },

    "scene_22_gorge_swim": {
        "name": "Eau Émeraude",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            "Two friends swimming in crystal clear emerald green water at a rocky gorge — "
            "a young man with light brown messy hair on the left facing slightly toward the girl, "
            f"and a {DORIANE_ADULT} with wet dark hair on the right, her head turned AWAY from camera "
            "so only the back of her head is visible, looking toward the waterfall ahead. "
            "Ahead of them, a massive grey limestone cliff face covered in green vegetation, "
            "a thin waterfall cascading down the rock into the pool. "
            "Crystal clear emerald-green water with beautiful reflections. "
            "Bright sunny day, warm golden light, volumetric god rays, rich vibrant colors."
        ),
        "video_prompt": (
            "A GTA V in-game cutscene third-person shot. Two friends seen from behind in emerald green water at a rocky gorge. "
            "Water ripples around them. The thin waterfall cascades down the cliff behind. "
            "Heavy GTA V film grain throughout — visible noise across the entire frame. "
            "RAGE engine textures, warm desaturated color grading. GTA V water shader with gentle ripples. "
            "Camera stays behind them, very slight movement. "
            "This looks like a GTA V gameplay recording — video game graphics, not photorealistic."
        ),
    },

    "scene_23_theme_park": {
        "name": "Jouets Géants",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            f"Two young women SEEN FROM BEHIND walking toward a colorful theme park entrance — "
            f"a {DORIANE_ADULT} with long dark hair in braids wearing a white graphic t-shirt and denim shorts on the left, "
            "and her friend with dark hair wearing a white t-shirt and grey shorts on the right. "
            "Ahead of them, a giant colorful cowboy character statue towering above, "
            "oversized colorful toy building blocks spelling out letters in red, yellow, green, blue, "
            "bright primary colors everywhere, bamboo and green vegetation surrounding the area. "
            "Bright sunny day, clear blue sky, warm vibrant colors, theme park atmosphere."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women walk forward toward a colorful theme park entrance with a giant cowboy statue. "
            "They walk steadily away from camera, never turning back. "
            "Colorful toy blocks and bright decorations on both sides. Bright sunny day. "
            "Camera follows smoothly from behind as they walk. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_24_golden_gate": {
        "name": "San Francisco",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            f"A couple SEEN FROM BEHIND standing on a hilltop viewpoint overlooking the Golden Gate Bridge — "
            f"a {DORIANE_ADULT} with dark hair in braids wearing a grey oversized sweatshirt, blue jeans and sunglasses on the left, "
            "and a tall young man with short buzzed hair wearing a black t-shirt on the right, "
            "his arm around her shoulder. "
            "Ahead of them, the iconic red Golden Gate Bridge stretching across the bay, "
            "fog rolling beneath the bridge towers, turquoise ocean water below, "
            "cars driving across the bridge, rolling green hills. "
            "Bright sunny day, clear blue sky, California golden light, subtle god rays."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A couple stands at a hilltop viewpoint overlooking the Golden Gate Bridge. "
            "Gentle wind blows her hair. Fog drifts slowly beneath the bridge towers. "
            "Cars move across the bridge. Light shifts subtly. "
            "Camera stays behind them, very slight drift. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_25_grand_canyon": {
        "name": "Grand Canyon",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            "Two young women SEEN FROM BEHIND standing at the edge of the Grand Canyon, "
            "both with arms raised wide open in celebration — "
            f"a {DORIANE_ADULT} with long dark hair wearing a brown Grand Canyon National Park souvenir t-shirt "
            "and light denim shorts on the left, arms around each other, "
            "and her blonde friend wearing a yellow baseball cap, matching brown souvenir t-shirt "
            "and black biker shorts on the right. "
            "Ahead of them, the breathtaking Grand Canyon stretches to the horizon — "
            "massive layered red and orange rock formations, deep gorges, "
            "the Colorado River visible far below, rocky cliff edge beneath their feet. "
            "Bright sunny day, clear blue sky with white clouds, epic American landscape scale, "
            "volumetric god rays, rich vibrant warm colors."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women stand at the edge of the Grand Canyon with arms raised wide. "
            "Gentle wind blows their hair and t-shirts. Light shifts subtly on the canyon walls. "
            "Epic landscape stretches to the horizon. Bright sunny day. "
            "Camera stays behind them, very slight drift. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_28_fete_foraine": {
        "name": "Fête Foraine — with Fiona",
        "type": "image-to-image",
        "source_image": "output/images/friends/scene_28_fete_foraine.png",
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters. "
            "Two teenage girls SEEN FROM BEHIND sitting inside a colorful dragon-themed ghost train cart "
            "at a fairground, about to enter the dark tunnel of the ride. "
            f"A {DORIANE_TEEN} with long dark brown wavy hair and bangs wearing a white t-shirt on the right, "
            "and her friend with long strawberry-blonde hair wearing a black vest over a light top on the left. "
            "Both facing forward, looking ahead into the ride entrance. "
            "Surrounding them: painted stone castle walls, large red dragon sculptures with glowing eyes, "
            "colorful medieval fantasy decorations, gargoyle faces on the ride panels. "
            "Fairground lights and carnival tents visible in the background. "
            "Warm summer evening light, vibrant fairground colors, fun carnival atmosphere. "
            "French countryside fairground at Les Issambres."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two teenage girls sit in a dragon-themed ghost train cart at a fairground. "
            "The cart moves slowly forward into the dark tunnel entrance, colorful lights flicker around them. "
            "Painted castle walls and dragon decorations pass by on both sides. Warm carnival atmosphere. "
            "Camera follows smoothly from behind as the cart moves. "
            "Stylized video game textures, PBR material shaders, GTA V style 3D rendering, "
            "next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_29_chicago_river": {
        "name": "Chicago with Gabrielle",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            "Two young women SEEN FROM BEHIND walking away from camera along a pedestrian bridge "
            "over the Chicago River. "
            f"On the left, a young woman with long dark hair and round sunglasses, "
            "wearing a light grey-lavender oversized jacket, olive cargo pants, and white sneakers. "
            f"On the right, a {DORIANE_ADULT} with long dark wavy hair, wearing a white crop top "
            "and a long black maxi skirt with black boots. "
            "Ahead of them, the Chicago River stretches into the distance between tall skyscrapers — "
            "modern glass towers, red brick loft buildings with green ivy climbing the walls, "
            "bridges crossing the river, a yellow water taxi on the green water below. "
            "Brown metal railing on both sides of the bridge. "
            "Bright sunny summer day, clear blue sky, warm golden light, volumetric god rays, "
            "rich vibrant colors, epic urban river canyon."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women walk forward together along the Chicago Riverwalk. "
            "They move steadily forward away from camera, never turning back. "
            "Tall glass skyscrapers and brick buildings tower on both sides of the river. "
            "A yellow water taxi passes by on the river. Bright sunny day, warm light. "
            "Camera follows smoothly from behind as they walk along the riverwalk. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_30_princesses": {
        "name": "Bridgerton Experience with Coline",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            "Two young women SEEN FROM BEHIND walking away from camera down a red-carpeted hallway "
            "into an opulent VIP lounge. "
            f"On the right, a {DORIANE_ADULT} with long dark wavy hair and a white satin hair bow, "
            "wearing a flowing white-lavender sparkly tulle princess gown with sheer sleeves and gold strappy heels. "
            "On the left, her friend with long dark hair and a crystal tiara, "
            "wearing a matching white-lavender sparkly tulle dress with floral embroidery and pink heels. "
            "Ahead of them, an ornate vintage velvet couch on a raised red carpet stage, "
            "deep red satin curtains draping the walls, crystal candelabras with glowing candles on both sides, "
            "pink and purple neon ambient lighting casting dramatic shadows. "
            "Gold ornate decorations, sparkles in the air, luxurious glamorous atmosphere. "
            "Rich vibrant magenta and purple color grading, subtle bloom on light sources."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women in flowing sparkly white-lavender princess gowns walk forward "
            "down a red-carpeted hallway toward an opulent VIP lounge. "
            "They move steadily forward away from camera, never turning back. "
            "Crystal chandeliers sparkle, pink and purple neon lights glow on the walls. "
            "Red satin curtains and gold decorations on both sides. Glamorous atmosphere. "
            "Camera follows smoothly from behind as they walk. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_31_rooftop_night": {
        "name": "Rooftop Party with Rocco & Hortense",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            "Three friends SEEN FROM BEHIND walking away from camera toward the edge of a rooftop bar at night. "
            f"On the left, a {DORIANE_ADULT} with long dark wavy hair and sunglasses, "
            "wearing a white t-shirt and denim shorts. "
            "In the middle, a young man with short dark hair, a light beard, wearing a dark navy sweatshirt "
            "and a black baseball cap with a small red logo. "
            "On the right, a young blonde woman with long straight blonde hair, "
            "wearing a black tank top, holding a drink can in her hand. "
            "Ahead of them, the edge of a rooftop bar terrace with floor-to-ceiling glass windows, "
            "a glowing city skyline at night — skyscrapers lit up, city lights reflecting on water in the distance, "
            "ambient bar lighting in warm tones, other people silhouetted in the background. "
            "Nighttime scene, neon glow, subtle bloom on light sources, moody urban atmosphere."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Three friends walk forward toward the edge of a rooftop bar at night. "
            "They move steadily forward away from camera, never turning back. "
            "City skyline glows through the glass windows ahead. Ambient bar lighting. "
            "Other patrons visible in the background. Moody nighttime atmosphere. "
            "Camera follows smoothly from behind as they walk. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    "scene_32_monument_valley_duo": {
        "name": "US Roadtrip with Silah",
        "type": "text-to-image",
        "source_image": None,
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            "A couple SEEN FROM BEHIND walking away from camera along a red dirt path "
            "toward the iconic Monument Valley buttes. "
            f"On the left, a {DORIANE_ADULT} with long dark curly hair, wearing a white oversized sweatshirt, "
            "red-white gingham shorts, white socks and white sneakers, one arm raised high in the air in celebration. "
            "On the right, a young mixed-race man with brown skin, medium build, slightly shorter than the woman, "
            "short dark hair, wearing a brown t-shirt, black shorts, and white sneakers. "
            "Ahead of them, the massive red sandstone buttes and mesas of Monument Valley rise from the desert floor, "
            "a rusty metal railing at the viewpoint edge, flat red earth stretching to the horizon. "
            "Overcast dramatic sky with heavy clouds, diffused warm light, "
            "epic American West landscape scale, rich vibrant red earth tones."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "A couple walks forward along a red dirt path toward Monument Valley buttes. "
            "They move steadily forward away from camera, never turning back. "
            "The woman has one arm raised in celebration. Wind blows her curly hair. "
            "Red sandstone buttes tower ahead. Overcast dramatic sky. "
            "Camera follows smoothly from behind as they walk. "
            "Next-gen video game graphics, clean crisp rendering."
        ),
    },

    # ===== NEW FRIENDS SCENES =====

    "scene_33_disneyland": {
        "name": "Disneyland — with Julie",
        "type": "image-to-image",
        "source_image": "output/images/friends/scene_33_disneyland.png",
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            f"Two young women SEEN FROM BEHIND walking through Disneyland Paris main street — "
            f"a {DORIANE_ADULT} on the left wearing Minnie Mouse ears headband, a navy blue puffer jacket "
            "over a striped top, dark leggings and red Converse sneakers, "
            "and her friend on the right with long straight brown hair wearing a denim jacket, "
            "dark ripped jeans and black Vans sneakers. "
            "Ahead of them, the iconic Disneyland Paris castle in the distance, "
            "colorful shop facades lining Main Street, Disney character mascots walking around, "
            "visitors and families in the crowd. "
            "Bright sunny day, festive theme park atmosphere, Disney magic."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women walk forward through Disneyland Paris main street toward the castle. "
            "They walk steadily away from camera, never turning back. "
            "Colorful shops and Disney decorations on both sides, visitors walking around. "
            "Bright sunny day, festive atmosphere. "
            "Camera follows smoothly from behind as they walk. "
            "Next-gen video game graphics, clean crisp rendering, vibrant colors."
        ),
    },

    "scene_34_paris_seine": {
        "name": "Seine by Night — with Laura",
        "type": "image-to-image",
        "source_image": "output/images/friends/scene_34_paris_seine.png",
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            "NO low-poly, NO cartoonish, NO stylized — ultra-realistic high-polygon 3D rendering with photorealistic skin, hair, and fabric textures. "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            f"Two young women SEEN FROM BEHIND standing at the railing of a Seine river cruise boat in Paris at dusk — "
            f"a {DORIANE_ADULT} on the left wearing a black leather jacket over a light blue floral daisy dress "
            "and a straw cowboy hat, "
            "and her friend on the right with dark hair wearing a black blazer, white crop top, "
            "light blue jeans and a beige cowboy hat. "
            "Both leaning on the boat railing, looking out toward the Eiffel Tower. "
            "Ahead of them, the Eiffel Tower glowing golden against a deep blue dusk sky, "
            "lights reflecting on the Seine river water, Parisian buildings along the riverbanks. "
            "Romantic twilight atmosphere, warm golden and cool blue tones. "
            "Hyper-detailed textures, subsurface scattering on skin, ray-traced reflections on water, cinematic depth of field."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women stand at the railing of a boat cruise on the Seine river in Paris. "
            "They look out at the glowing Eiffel Tower ahead. The boat moves gently forward on the water. "
            "Golden reflections shimmer on the river surface. Twilight sky deepens. "
            "Camera stays behind them, gentle drift with the boat motion. "
            "Next-gen video game graphics, clean crisp rendering, romantic atmosphere."
        ),
    },

    "scene_35_nyc_rooftop": {
        "name": "NYC Sunset — with Alison",
        "type": "image-to-image",
        "source_image": "output/images/friends/scene_35_nyc_rooftop.png",
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            f"Two young women SEEN FROM BEHIND standing on a rooftop terrace in Manhattan at sunset — "
            f"a {DORIANE_ADULT} on the left with long dark hair under a yellow baseball cap, "
            "wearing a black oversized hoodie, "
            "and her friend on the right with light brown hair in a bun wearing a navy blue Guess Jeans sweatshirt. "
            "Both leaning on the rooftop ledge, looking out at the skyline. "
            "Ahead of them, the Manhattan skyline stretching to the horizon — "
            "glass skyscrapers with lit windows, H&M neon sign visible, "
            "dramatic pink and purple sunset sky with orange glow near the horizon. "
            "Golden hour rooftop atmosphere, city lights starting to glow."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women stand on a Manhattan rooftop at sunset looking out at the skyline. "
            "Pink and purple clouds drift slowly. City lights flicker on across the buildings. "
            "Wind gently moves their hair. The sunset glow fades gradually. "
            "Camera stays behind them, very slight drift. "
            "Next-gen video game graphics, clean crisp rendering, dramatic sunset colors."
        ),
    },

    "scene_36_miami_ocean": {
        "name": "Miami Beach",
        "type": "image-to-image",
        "source_image": "output/images/friends/scene_36_miami_ocean.png",
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            "Stylized 3D video game rendering, soft painterly textures, NOT a photograph, clearly a video game screenshot. "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            f"Two young women SEEN FROM BEHIND standing on a balcony of a white beachfront villa "
            "looking out at the turquoise ocean — "
            f"a {DORIANE_ADULT} on the left with long dark hair and sunglasses on her head, "
            "wearing a black summer dress, "
            "and her friend on the right with blonde shoulder-length hair wearing a blue tie-dye mini dress "
            "and a small beige crossbody bag. "
            "Ahead of them, stunning turquoise Caribbean ocean stretching to the horizon, "
            "palm trees swaying, white sand beach below, tropical blue sky with volumetric clouds. "
            "Warm golden sunlight, soft atmospheric haze over the water, gentle bloom, cinematic depth of field. "
            "Bright tropical day, soft dreamy atmosphere."
        ),
        "video_prompt": (
            "Third-person gameplay camera following from behind. "
            "Two young women stand on a villa balcony looking out at the turquoise ocean. "
            "Gentle tropical breeze moves their hair and dresses. Waves shimmer in the distance. "
            "Bright sunny day, white clouds drift slowly. "
            "Camera stays behind them, very slight drift. "
            "Next-gen video game graphics, clean crisp rendering, tropical vibrant colors."
        ),
    },

    # ===== FRIENDS — PUNTA CANA =====

    "scene_37_punta_cana_duo": {
        "name": "Punta Cana — with a Friend",
        "type": "image-to-image",
        "source_image": "output/images/friends/scene_37_punta_cana_duo.png",
        "aspect_ratio": "16:9",
        "duration": "8",
        "image_prompt": (
            f"{STYLE} "
            "Stylized 3D video game rendering, soft painterly textures, NOT a photograph, clearly a video game screenshot. "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            f"Two young women SEEN FROM BEHIND leaning against a warm terracotta-orange stucco wall "
            "in a tropical Caribbean resort town — "
            f"a {DORIANE_ADULT} on the left with braided hair pulled back, small oval retro sunglasses, "
            "wearing a colorful floral mini dress (orange, green, pink, purple flowers), "
            "and her friend on the right with dark hair, black heart-shaped sunglasses, "
            "wearing a crochet halter crop top and yellow lace shorts, feather earrings. "
            "Both posing casually, one hand on hip. "
            "Warm orange wall filling the background, harsh tropical midday sun casting short shadows. "
            "Hot summer festival vibes, saturated warm tones, golden sunlight, soft atmospheric glow."
        ),
        "video_prompt": (
            "Third-person gameplay camera following two young women from behind as they walk on a white sand tropical beach. "
            "Palm trees sway gently in the warm breeze. Turquoise Caribbean waves lap at the shore. "
            "Bright tropical sunlight, golden warm tones. Hair and dresses move with the breeze. "
            "Camera follows slowly, gentle drift. "
            "Next-gen video game graphics, cinematic rendering, warm saturated tropical colors."
        ),
    },

    "scene_38_punta_cana_group": {
        "name": "Punta Cana — Wedding Party",
        "type": "text-to-image",
        "aspect_ratio": "16:9",
        "duration": "5",
        "image_prompt": (
            f"{STYLE} "
            "Stylized 3D video game rendering, soft painterly textures, NOT a photograph, clearly a video game screenshot. "
            "SEEN FROM BEHIND — third-person gameplay camera positioned several meters behind "
            "and slightly above the characters, classic GTA V walking perspective. "
            "A group of five friends and a baby SEEN FROM BEHIND standing together on a wooden boardwalk deck "
            "at a tropical Caribbean resort at sunset — "
            "Far left: a woman with light brown hair and a white lace headband, wearing an emerald green summer dress "
            "and navy flat sandals. "
            f"Second from left: a {DORIANE_ADULT} wearing a black crop top and light blue-white lace shorts, "
            "beige heeled sandals. "
            "Center: a tall Caucasian white-skinned man with short brown hair, seen from behind — "
            "he wears a DARK NAVY BLUE suit jacket (very dark blue, almost black), "
            "with a bright WHITE dress shirt underneath visible at the collar and between the lapels, "
            "a small BLACK bow tie tied at the neck against the white shirt, "
            "a single small white rose boutonnière pinned on the left lapel of the dark jacket, "
            "dark dress pants matching the jacket, black leather dress shoes. "
            "Fourth: an East Asian woman with straight dark hair and round glasses, light skin, wearing a colorful tropical floral maxi dress "
            "(dark with purple, green, pink leaves), colorful sneakers. "
            "Far right: a Black woman with long dark braids, wearing a teal emerald green off-shoulder dress, "
            "holding a baby in a light blue outfit on her hip. "
            "All five standing close together in a line, arms around each other's shoulders, "
            "looking out toward the tropical resort grounds ahead. "
            "Palm trees swaying in warm evening breeze, golden sunset sky with soft pink and orange clouds, "
            "tropical resort with pool area visible in the distance. "
            "Warm golden-hour lighting, soft atmospheric haze, cinematic depth of field, "
            "tropical celebration atmosphere."
        ),
        "video_prompt": (
            "Third-person gameplay camera positioned behind a group of five friends "
            "as they walk FORWARD AWAY from the camera together on a wooden boardwalk at a tropical resort at sunset. "
            "The group moves FORWARD into the scene, walking slowly side by side toward the resort, arms around each other. "
            "Palm trees sway gently in the warm breeze. Golden sunset sky with pink clouds. "
            "Camera stays still as they walk away into the distance. "
            "Next-gen video game graphics, cinematic rendering, warm golden tropical colors."
        ),
    },
}
