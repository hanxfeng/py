from PIL import Image
import os
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np

#输出需要图片地址，图片名称，标注框信息，类别
def tupian(data_path,csv_path):
    info_array=[]
    col=['filename','filepath','label']
    classes = os.listdir(data_path)
    for kindname in os.listdir(data_path):
        classpath = os.path.join(data_path, kindname)
        for filename in os.listdir(classpath):
            filepath = os.path.join(classpath, filename)
            label = classes.index(kindname)
            info_array.append([filename, filepath, label])
    info_array = np.array(info_array)
    df = pd.DataFrame(info_array, columns=col)
    df.to_csv(csv_path, encoding='utf-8')
    #读取标注框
def xmlpath(xml_path,csv_path):
    a=[]
    b=[]
    col=['filepath','filename','xmin','xmax','ymin','ymax']
    for filename in os.listdir(xml_path):
        xml2_path=os.path.join(xml_path,filename)
        tree = ET.parse(xml2_path)
        root=tree.getroot()
        for obj in root.findall('object'):
            bndbox = obj.find('bndbox')
            if bndbox is not None:
                xmin = int(bndbox.find('xmin').text)
                xmax = int(bndbox.find('xmax').text)
                ymin = int(bndbox.find('ymin').text)
                ymax = int(bndbox.find('ymax').text)
                a.append([xml2_path,filename,xmin,xmax,ymin,ymax])
        filename = root.find('path').text
        filename=filename.replace('..','')
        b.append(filename)
    cc=['data_path']
    df1=pd.DataFrame(b,columns=cc)
    df = pd.DataFrame(a, columns=col)#, columns=col
    df.to_csv(csv_path, encoding='utf-8')
    df1.to_csv(r'D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\标注框2.csv',encoding='utf-8')

#if __name__ == '__main__':
#    tupian(r"D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\train",r'D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\图片.csv')
#    xmlpath(r"D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\train_xmls",r'D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\标注框.csv')
#        #读取图片并调整至统一大小
def duqu(csv_path,out_path):
    a=pd.read_csv(csv_path,encoding='GB2312')
    b=a['data_path']
    i=0
    e=[]
    while i<1325:
        c=r"D:\a\data"
        filepath=b[i]
        path=r'D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注'+filepath
        xmin=a['xmin'][i]
        xmax=a['xmax'][i]
        ymin=a['ymin'][i]
        ymax=a['ymax'][i]
        img=Image.open(path)
        d=c+filepath

        #图片大小调整
        new_width = 800
        new_height = 800
        resized_image = img.resize((new_width, new_height), Image.LANCZOS)
        resized_image.save(d)
        #标注框调整

        width, height = img.size
        scale_width = new_width / width
        scale_height = new_height / height
        new_xmin = int(xmin * scale_width)
        new_ymin = int(ymin * scale_height)
        new_xmax = int(xmax * scale_width)
        new_ymax = int(ymax * scale_height)

        # 确保坐标不超出图片边界
        new_xmin = max(0, new_xmin)
        new_ymin = max(0, new_ymin)
        new_xmax = min(new_width, new_xmax)
        new_ymax = min(new_height, new_ymax)

        e.append([d,new_xmin,new_xmax,new_ymin,new_ymax])
        i=i+1
        #col=['filepath','new_xmin','new_xmax','new_ymin','new_ymax']
    df=pd.DataFrame(e)
    df.to_csv(out_path)


if __name__ == '__main__':
    duqu(r"D:\a\data\2024服创大赛A03井盖数据完整\脱敏井盖训练数据及标注\标注框.csv",r"D:\a\data\1.csv")

    #调整标注框
    #输出