import os
from torchvision import transforms
import torch
from torch.utils.data import Dataset
from torch.utils.data import  DataLoader
import pandas as pd
import numpy as np
import cv2
from PIL import Image


#init：其中通常需要传入数据和数据所在目录

class Dataset_b(Dataset):
    def __init__(self,dataset_dir,csv_path,resize_shape):
        self.dataset_dir=dataset_dir
        self.csv_path=csv_path
        self.shape=resize_shape#将图片调整到指定大小
        self.df=pd.read_csv(self.csv_path,encoding='utf-8')
        self.transformer = transforms.Compose([
            #transforms.Grayscale(num_output_channels=1),  # 将图片转换为灰度图
            transforms.Resize(self.shape),
            transforms.ToTensor(),#将图片或np数组转换为张量
        ])

    def __getitem__(self,idx):
        x_train=self.transformer(Image.open(self.df.iloc[idx]['filepath']))
        y_train=self.df.iloc[idx]['label']
        return x_train,y_train

    def __len__(self):
        return len(self.df)#self.后为init中标签的变量名/图片数据的变量名


class Dataset_c(Dataset):
    def __init__(self,data_path,csv_path,en,target_transform=None):
        self.data_path=data_path
        self.csv_path=csv_path
        self.df=pd.read_csv(self.csv_path,encoding=en)
        self.target_transform = target_transform
        self.transformer=transforms.Compose([
            transforms.Resize((800, 800)),
            transforms.ToTensor(),
            #transforms.Lambda(lambda t: t.unsqueeze(0)),

        ])

    def __getitem__(self, idx):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        data=self.transformer(Image.open(self.df.iloc[idx]['filepath']))
        label = self.df.iloc[idx]['label']
        boxes = self.df.iloc[idx][['xmin', 'ymin', 'xmax', 'ymax']]
        bbox = torch.tensor(boxes,dtype=torch.float32).unsqueeze(0).to(device)#.unsqueeze(0)
        label = torch.tensor(label,dtype=torch.int64).to(device)

        return data,bbox,label
    def __len__(self):
        return  len(self.df)

    def load_and_transform_image(self, filepath):
        image = Image.open(filepath)
        data = self.transformer(image)
        return data






#train_set=Dataset_a(r"D:\a\data\xin",r"D:\a\csv\fwwb.csv",(1080,1080))
#print(len(train_set))
# DataLoader参数：
# dataset：Dataset函数所创建的对象
#batch_size：每次从Dataset中拿出的数据数量
#num_workers：设定使用的cpu线程数，最高取决于cpu个数，默认为0
#shuffle:是否对数据进行打乱，true 是 false  否  测试集一般不随机
#sampler：决定如何对数据进行采样（默认即可）
#batch_sampler：同上
#pin_memory:是否将数据储存在cpu中，默认false，当数据量大时不要改为true，当为true时对速度提升不明显
#drop_last:默认false，当设置为true时，若Dataset中的数据不为batch_size的整数倍时，将剩余数据丢弃
#collate_fn:对batch_size的数据进行再次处理
