import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import cv2
import os

def load_image(image_path, max_dim=512):
    """Loads and preprocesses an image efficiently."""
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        print("Available files in the current directory:", os.listdir(os.getcwd()))
        raise FileNotFoundError(f"Check the filename and try again.")
    
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB format
    img = cv2.resize(img, (max_dim, max_dim), interpolation=cv2.INTER_AREA)
    img = img.astype(np.float32) / 255.0
    return img[np.newaxis, ...]

def save_image(image, output_path):
    """Saves the processed image with high efficiency."""
    img = Image.fromarray((image[0] * 255).astype(np.uint8))
    img = img.filter(ImageFilter.SHARPEN)
    img.save(output_path, quality=95)
    print(f"Image saved successfully at: {output_path}")

def apply_advanced_style():
    """Gets user input and applies an optimized style transfer effect with adjustable intensity."""
    content_path = input("Enter the path to the content image: ")
    style_path = input("Enter the path to the style image: ")
    output_path = input("Enter the path to save the stylized image: ")
    alpha = float(input("Enter blending intensity for content (0 to 1, default 0.7): ") or 0.7)
    beta = float(input("Enter blending intensity for style (0 to 1, default 0.3): ") or 0.3)
    
    print("Loading images...")
    content_image = load_image(content_path)
    style_image = load_image(style_path)
    
    print("Resizing style image to match content dimensions...")
    style_resized = cv2.resize(style_image[0], (content_image.shape[2], content_image.shape[1]), interpolation=cv2.INTER_AREA)
    
    print("Applying optimized blending...")
    blended_image = cv2.addWeighted(content_image[0], alpha, style_resized, beta, 0)
    
    print("Applying artistic enhancements...")
    pil_image = Image.fromarray((blended_image * 255).astype(np.uint8))
    pil_image = pil_image.filter(ImageFilter.DETAIL)
    pil_image = pil_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    pil_image = pil_image.filter(ImageFilter.SMOOTH_MORE)
    pil_image = pil_image.filter(ImageFilter.SHARPEN)
    
    final_image = np.array(pil_image) / 255.0
    
    print("Saving final stylized image...")
    save_image(final_image[np.newaxis, ...], output_path)
    
    plt.figure(figsize=(8, 8))
    plt.imshow(final_image)
    plt.axis('off')
    plt.show()
    print("Style transfer complete!")

if __name__ == "__main__":
    apply_advanced_style()
