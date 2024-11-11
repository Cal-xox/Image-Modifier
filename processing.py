from PIL import Image, ImageEnhance
import os

directory = r"C:\Users\Calvin\Documents\Image-Modifier\textures"
reset = r"C:\Users\Calvin\Documents\Image-Modifier\base"

print("Enter the factor for modifying the brightness of the files:")
userinput = float(input())



for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    file = os.path.join(filename)
    if os.path.isfile(f):
        enhancer = ImageEnhance.Brightness(Image.open(f))
        enhancer.enhance(userinput).save(os.path.join(directory, file));
        print(file)

userRestInput = str(input("Do you want to reset the brightness of the files? (y/n)"))

if userRestInput == "y":
    for filename in os.listdir(reset):
        f = os.path.join(reset, filename)
        file = os.path.join(filename)
        if os.path.isfile(f):
            enhancer = ImageEnhance.Brightness(Image.open(f))
            enhancer.enhance(1).save(os.path.join(directory, file));
            print(file)

print("Done")
