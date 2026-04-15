export const ENGINE_MODEL_IDS = {
    imagen4: "imagen-4.0-generate-001",
    "imagen4-fast": "imagen-4.0-fast-generate-001",
    "imagen4-ultra": "imagen-4.0-ultra-generate-001",
};
export const ASPECT_RATIOS = ["16:9", "4:3", "1:1", "9:16", "3:4"];
export const IMAGE_STYLE_PROMPTS = {
    realistic: "Create a hyper-realistic photograph with exceptional detail and clarity.",
    illustration: "Create a hand-drawn illustration with warm, inviting atmosphere and artistic charm.",
    flat: [
        "Create a simple, minimal but a little pop illustration with a white background.",
        "Use soft pastel colors with gentle saturation, incorporating light blue, mint green",
        "and soft pink as accent colors. The style should feature rounded lines and delicate",
        "details, creating a friendly and approachable look that's both modern and charming.",
        "The illustration should be easily recognizable while maintaining a sweet, cheerful simplicity.",
    ].join(" "),
    anime: "Create an image in Japanese anime style with vibrant colors and distinctive eye designs.",
    watercolor: "Create a watercolor painting with soft, flowing colors and artistic blending effects.",
    "oil-painting": "Create an oil painting with rich textures, deep colors, and impasto effects.",
    "pixel-art": "Create a pixel art image with retro gaming aesthetics and digital precision.",
    sketch: "Create a pencil or pen sketch with dynamic line variations and artistic expression.",
    "3d-render": "Create a 3D rendered image with realistic lighting, materials, and depth.",
    corporate: "Create a professional business image with clean, modern aesthetics and corporate appeal.",
    minimal: "Create a minimal design with clean lines, essential elements, and refined simplicity.",
    "pop-art": "Create a pop art image with bold colors, dot patterns, and contemporary style.",
};
export const FORMAT_MIME = {
    png: "image/png",
    jpg: "image/jpeg",
    jpeg: "image/jpeg",
};
export const GEMINI_MODEL = "gemini-2.5-flash";
