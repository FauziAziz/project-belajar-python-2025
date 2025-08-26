from PIL import Image, ImageEnhance, ImageOps
import colorsys

def adjust_exposure(image, factor):
    """Adjust exposure of the image."""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    """Adjust contrast of the image."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def adjust_tone(image, tone_shift):
    """Adjust tone of the image by shifting RGB values."""
    def shift_tone(pixel):
        r, g, b = pixel
        return (r + tone_shift[0], g + tone_shift[1], b + tone_shift[2])
    return image.point(shift_tone)

def adjust_hsl(image, hue_shift=0, saturation_factor=1.0, lightness_factor=1.0):
    """Adjust HSL (Hue, Saturation, Lightness) of the image."""
    def shift_hsl(pixel):
        r, g, b = [x / 255.0 for x in pixel]  # Normalize
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        h = (h + hue_shift) % 1.0
        s = max(0.0, min(1.0, s * saturation_factor))
        l = max(0.0, min(1.0, l * lightness_factor))
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return int(r * 255), int(g * 255), int(b * 255)

    return image.convert('RGB').point(lambda x: shift_hsl((x, x, x)))

# Load image
image_path = "your_image.jpg"  # Ganti dengan path gambar
image = Image.open(image_path)

# Apply filters
image_exposed = adjust_exposure(image, 1.5)  # Exposure
image_contrast = adjust_contrast(image_exposed, 1.2)  # Contrast
image_tone = adjust_tone(image_contrast, (10, -5, -20))  # Adjust tone (RGB shift)
image_hsl = adjust_hsl(image_tone, hue_shift=0.1, saturation_factor=1.2, lightness_factor=1.1)  # Adjust HSL

# Save the result
output_path = "filtered_image.jpg"
image_hsl.save(output_path)
image_hsl.show()

print(f"Filtered image saved to {output_path}")
