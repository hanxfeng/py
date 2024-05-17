import cv2
import os
import numpy as np
from PIL import Image

def daxiao(input,out_dizhi):
    new_width=1075
    new_height=629
    image_files = [f for f in os.listdir(input) if os.path.isfile(os.path.join(input, f)) and f.lower().endswith(('.png', '.jpg'))]
    for image_file in image_files:
        image_path = os.path.join(input, image_file)
        img = Image.open(image_path)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        save=image_path = os.path.join(out_dizhi, image_file)
        img.save(save)

daxiao(r"C:\Users\韩行风\Desktop\1",r"C:\Users\韩行风\Desktop")

