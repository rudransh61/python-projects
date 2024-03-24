import numpy as np
from PIL import Image

# Load the target image (green circle on white background)
target_image = Image.open("circle.jpg").convert("RGB")

# Function to calculate percentage correctness
def calculate_percentage_correctness(generated_image_path):
    # Load the generated image
    generated_image = Image.open(generated_image_path).convert("RGB")
    
    # Resize the generated image to match the target image dimensions (200x200)
    generated_image_resized = generated_image.resize((200, 200))
    
    # Resize the target image to match the generated image dimensions
    target_image_resized = target_image.resize(generated_image_resized.size)
    
    # Convert images to numpy arrays for pixel-wise comparison
    np_generated_image = np.array(generated_image_resized)
    np_target_image = np.array(target_image_resized)
    
    # Count the number of pixels that are the same between the generated and target images
    num_same_pixels = np.sum(np.all(np_generated_image == np_target_image, axis=-1))
    
    # Calculate total number of pixels in the images
    total_pixels = np_generated_image.shape[0] * np_generated_image.shape[1]
    
    # Calculate percentage correctness
    percentage_correctness = (num_same_pixels / total_pixels) * 100
    
    return percentage_correctness

# Example usage:
generated_image_path = "img/result_image508.png"  # Path to the generated image
percentage_correctness = calculate_percentage_correctness(generated_image_path)
print("Percentage Correctness:", percentage_correctness)
