from PIL import Image, ImageEnhance
import os

directory = r"C:\Users\calxo\Documents\Image-Modifier\textures"
reset = r"C:\Users\calxo\Documents\Image-Modifier\base"

print("Enter the factor for modifying the brightness of the files:")
userinput = float(input())



for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    file = os.path.join(filename)
    if os.path.isfile(f):
        print(file)
    
