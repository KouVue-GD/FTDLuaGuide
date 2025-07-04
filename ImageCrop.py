from PIL import Image
import os

image_folder = input("Image folder path: ")

#(left, upper, right, lower)
crop_box = (200, 80, 1905, 1050)

os.makedirs(output_folder, exist_ok = True)

for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(image_folder, filename)
        with Image.open(path) as img:
            cropped = img.crop(crop_box)
            cropped.save(path)
