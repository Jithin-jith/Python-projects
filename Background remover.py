from rembg import remove
from PIL import Image

# Load the input image
input_path = "Tiger.jpg"  # Change this to your image path
output_path = "Tiger_background_removed.png"  # Output with transparent background

# Open the image
image = Image.open(input_path)

# Remove the background
output = remove(image)

# Save the output image
output.save(output_path)

print("Background removed successfully. Saved as", output_path)