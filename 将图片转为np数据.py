import numpy as np
import tensorflow as tf
from keras import datasets, layers, models  # 这里keras版本是2.8.0
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2

def Image_reading(input_image,out_image):
    image_files = [f for f in os.listdir(input_image) if f.endswith(('.png', '.jpg'))]#os.listdir:列出所有目录和子目录名称。f.endswith检查字符串是否以指定后缀结尾
    for image_file in image_files:
        image_path = os.path.join(input_image, image_file)#os.path.join：将路径连接（可以认为是展开子文件夹）,主文件在前，子文件在后
        image = cv2.imread(image_path)#将图片文件读取为np数组
        if image is None:
            print(f"Warning: Unable to read image at {image_path}")
            continue       #用于处理图像读取失败
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #将np数组由BGR转为RGB
        output_path = os.path.join(out_image, f"{image_file.split('.')[0]}.npy")#设置np数组存储路径
        np.save(output_path, image)#保存
Image_reading(r"D:\a\data\xin\good", r"D:\a\np\good")
Image_reading(r"D:\a\data\xin\lose", r"D:\a\np\lose")
Image_reading(r"D:\a\data\xin\uncovered", r"D:\a\np\uncovered")
Image_reading(r"D:\a\data\xin\circle", r"D:\a\np\circle")
Image_reading(r"D:\a\data\xin\broke", r"D:\a\np\broke")
