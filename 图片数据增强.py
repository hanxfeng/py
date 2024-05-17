from PIL import Image,ImageFilter,ImageEnhance
import os
from 重命名 import ming,ming2
from 文件转移 import zhuanyi
# 设置输入和输出文件夹路径

# 确保输出文件夹存在
def shujuzeng(input_folder,ouput_folder,i):
    if not os.path.exists(ouput_folder):
        os.makedirs(ouput_folder)

    # 遍历输入文件夹中的所有图像文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # 根据需要添加其他格式
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(ouput_folder, filename)

            # 打开图像文件
            with Image.open(input_path) as img:
                # 批量处理操作：例如调整大小、裁剪或转换为灰度图像等
                # 这里可以根据需要添加任意数量的处理步骤

                # 例如：调整图像大小
                img_resized = img.rotate(i,expand=True,fillcolor=(255, 255, 255))  # 翻转图像
                #img_resized=img.filter(ImageFilter.GaussianBlur(radius=5)) #高斯模糊
                #enhancer = ImageEnhance.Contrast(img)
                #img_resized = enhancer.enhance(1.3)


                # 保存处理后的图像
                img_resized.save(output_path)  # 或者使用 img_cropped.save(output_path) 或 img_gray.save(output_path)
i=45
while i<360:

    shujuzeng(r"D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\train\circle",r"D:\a\csj",i)

    #目前进度 3 4 5 6 7 8 9 10

    ming2(r"D:\a\csj")

    zhuanyi(r"D:\a\csj",r"D:\a\data\train\circle")


    ming(r"D:\a\data\train\circle")

    print(f'目前进度：{i}'.format(i=i))
    i=i+45
