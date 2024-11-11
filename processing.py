import os
from PIL import Image, ImageEnhance
import shutil

# Directories
directory = r"C:\Users\calxo\AppData\Roaming\pc7\PC7Swap\textures"
reset = r"C:\Users\calxo\AppData\Roaming\pc7\PC7Swap\base"
grid = r"C:\Users\calxo\AppData\Roaming\pc7\PC7Swap\grid"

def enhance_brightness(image_path, factor):
    """Open an image, enhance its brightness, and save it."""
    with Image.open(image_path) as img:
        # Convert image to RGB if it's not in that mode
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        enhancer = ImageEnhance.Brightness(img)
        enhanced_img = enhancer.enhance(factor)
        enhanced_img.save(image_path)  # Save the image over the original
        print(f"Enhanced brightness of {os.path.basename(image_path)}")

# Ask the user what to do (grid, default, or skip)
userRestInput = input("Do you want grid or default textures or skip(g/d/s)? ").lower()

# Handle the user's choice for textures
if userRestInput == "g":
    for filename in os.listdir(grid):
        f = os.path.join(grid, filename)
        if os.path.isfile(f):
            save_path = os.path.join(directory, filename)
            # Check if the file already exists in the directory, and delete it if it does
            if os.path.exists(save_path):
                os.remove(save_path)  # Remove the existing file
            
            # Process and move the file
            enhance_brightness(f, 1)  # No brightness change needed, so keep it as is
            shutil.copy2(f, save_path)  # Copy the modified image to the directory, overwriting the old file

elif userRestInput == "d":
    for filename in os.listdir(reset):
        f = os.path.join(reset, filename)
        if os.path.isfile(f):
            save_path = os.path.join(directory, filename)
            # Check if the file already exists in the directory, and delete it if it does
            if os.path.exists(save_path):
                os.remove(save_path)  # Remove the existing file
            
            # Process and move the file
            enhance_brightness(f, 1)  # No brightness change needed, so keep it as is
            shutil.copy2(f, save_path)  # Copy the modified image to the directory, overwriting the old file

elif userRestInput == "s":
    print("Awesome, skipping texture modification.")

# Now handle brightness modification for directory textures
userRestInput = input("Do you want modify colours or skip (m/s)? ").lower()
if userRestInput == "m":
    # Get user input for the brightness factor
    user_input = float(input("Enter the factor for modifying the brightness of the files: "))
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            enhance_brightness(f, user_input)
else:
    print("Awesome, skipping texture modification.")

print("Done")
