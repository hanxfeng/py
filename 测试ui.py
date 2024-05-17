import os.path
import sys
import numpy as np
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from frcnn_resent50 import FRCNN_resnet50
from frcnn_vgg16 import FRCNN_vgg16
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog,QLabel, QMainWindow,QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal,QObject
from PyQt5.QtGui import QIcon
from PIL import Image


class yuxing(QThread):

    finished = pyqtSignal(int)
    end=pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.input_images = None
        self.out_txt = None


    def run(self):
        with open('path/botn_data_path1.txt', 'r', encoding='utf-8') as file:
            aa = file.read()
            self.input_images = aa
        with open('path/botn_data_path2.txt', 'r', encoding='utf-8') as file:
            bb = file.read()
            self.out_txt = bb
        label_ = []
        conf_ = []
        xmin = []
        ymin = []
        xmax = []
        ymxa = []
        name = []
        zzz=1
        frcnn_vgg16 = FRCNN_vgg16()
        frcnn_resnet50 = FRCNN_resnet50()
        for file in os.listdir(self.input_images):
            path = os.path.join(self.input_images, file)
            image = Image.open(path)
            print(path)
            r_image1, xmin1, ymin1, xmax1, ymax1, score1, label1 = frcnn_vgg16.detect_image(image)
            r_image2, xmin2, ymin2, xmax2, ymax2, score2, label2 = frcnn_resnet50.detect_image(image)
            if score1 > score2:
                xmin.append(xmin1)
                ymin.append(ymin1)
                xmax.append(xmax1)
                ymxa.append(ymax1)
                conf_.append(score1)
                label_.append(label1)
                name.append(file)
            elif score1 < score2:
                xmin.append(xmin2)
                ymin.append(ymin2)
                xmax.append(xmax2)
                ymxa.append(ymax2)
                conf_.append(score2)
                label_.append(label2)
                name.append(file)
            self.finished.emit(zzz)
            zzz=zzz+1
        timae = time.strftime("%Y-%m-%d-%H-%M-%S")
        naa = f'{timae}.txt'
        txtpath = self.out_txt + '/' + naa
        with open(txtpath, 'w', encoding='utf-8') as file:
            for item1, item2, item3, item4, item5, item6, item7 in zip(name, label_, conf_, xmin, ymin, xmax, ymxa):
                file.write(f"{item1}\t{item2}\t{item3}\t{item4}\t{item5}\t{item6}\t{item7}\n")
        self.end.emit()

class FileSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = yuxing()
        self.thread.finished.connect(self.bar_bar)
        self.thread.end.connect(self.ending)
        self.input_images = None  # 初始化属性
        self.out_txt = None
        self.out_data=None
        self.i=None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('井盖识别')
        icon = QIcon('path/mls.jpg')
        self.setWindowIcon(icon)
        vbox = QVBoxLayout()                                        #创建一个垂直布局
        # 创建一个按钮，点击时触发文件选择对话框
        self.btn_select_file = QPushButton('选择图片所在文件夹', self) #创建一个按钮并显示 选择图片所在文件夹
        self.btn_select_file.setFixedSize(QSize(200, 30))          #设置按钮尺寸
        self.btn_select_file.clicked.connect(self.select_file)     #如果写成(self.select_file())会不显示界面直接执行程序，点击按钮后执行select_file函数
        vbox.addWidget(self.btn_select_file)                       #将按钮添加进垂直布局
        if os.path.isfile('path/botn_data_path1.txt'):
            with open('path/botn_data_path1.txt','r',encoding='utf-8')as file:
                aa=file.read()
                self.input_images = aa
                self.lable1=QLabel(aa)
        else:
            self.lable1=QLabel('未选择文件夹')                        #创建一个标签并显示 未选择文件夹
        vbox.addWidget(self.lable1)                                #将标签加入垂直布局

        self.btn_san=QPushButton('选择结果输出文件夹')
        self.btn_san.setFixedSize(QSize(200, 30))
        self.btn_san.clicked.connect(self.select_file3)
        vbox.addWidget(self.btn_san)
        if os.path.isfile('path/botn_data_path2.txt'):
            with open('path/botn_data_path2.txt', 'r', encoding='utf-8') as file:
                aa = file.read()
                self.out_txt = aa
                self.lable3 = QLabel(aa)
        else:
            self.lable3 = QLabel('未选择文件夹')
        vbox.addWidget(self.lable3)

        self.btn_si=QPushButton('点击运行',self)
        self.btn_si.setFixedSize(QSize(200, 30))
        self.btn_si.clicked.connect(self.select_file4)
        vbox.addWidget(self.btn_si)
        self.lable4=QLabel('程序尚未运行')
        vbox.addWidget(self.lable4)

        self.bar= QProgressBar(self)                          #添加一个进度条
        self.bar.setRange(0, 100)           #将进度条设置为0-100
        vbox.addWidget(self.bar)                              #将进度条添加至布局

        self.btn_wu=QPushButton('选择需要分类的文件',self)
        self.btn_wu.setFixedSize(QSize(200,30))
        self.btn_wu.clicked.connect(self.select_file5)
        vbox.addWidget(self.btn_wu)
        self.lable5=QLabel('尚未选择需分类的文件')
        vbox.addWidget(self.lable5)

        self.setLayout(vbox)#设置布局
        self.resize(400, 300)#设置窗口大小

    def select_file(self):
            directory = QFileDialog.getExistingDirectory(self, "选择图片所在文件夹")
            if directory:
                self.input_images = directory  # 将选择的目录赋值给类的属性
                with open('path/botn_data_path1.txt', 'w', encoding='utf-8') as file:
                    file.write(directory)
                self.lable1.setText(directory)

    def select_file3(self):
        directory = QFileDialog.getExistingDirectory(self, "选择结果输出文件夹")  #打开一个文件选择器，并将选择的文件地址写入directory
        if directory:
            self.out_txt = directory  # 将选择的目录赋值给类的属性
            with open('path/botn_data_path2.txt', 'w', encoding='utf-8') as file:
                file.write(directory)
            self.out_data = directory
            self.lable3.setText(directory)                              #将lable3的文本设置为directory的值

# pyinstaller -w 测试ui.py

    def select_file4(self):
        if os.path.isfile('path/botn_data_path1.txt')and os.path.isfile('path/botn_data_path2.txt'):
            if not self.thread.isRunning():
                self.thread.start()                                 #启动线程
                self.lable4.setText('程序正在运行中')                  #更新按钮信息
                self.btn_si.setEnabled(False)                          #禁用按钮点击
                self.thread.finished.connect(self.next)             #结束后执行括号内的函数
            else:
                self.lable4.setText('请勿重复点击')
        else:
            self.lable4.setText('请先选择必要文件夹')

    def select_file5(self):
        directory,_=QFileDialog.getOpenFileName(self,'选择文件','',"Text Files (*.txt)")
        a = []
        with open(directory, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split()
                data = data[:7]
                a.append(data)
        good = []
        broke = []
        lose = []
        uncovered = []
        circle = []
        i = 0
        for i in range(0, len(a)):
            if int(a[i][1]) == 0:
                good.append(a[i])
            elif int(a[i][1]) == 1:
                broke.append(a[i])
            elif int(a[i][1]) == 2:
                lose.append(a[i])
            elif int(a[i][1]) == 3:
                uncovered.append(a[i])
            elif int(a[i][1]) == 4:
                circle.append(a[i])
        file_name,_=os.path.splitext(os.path.basename(directory))
        path=os.path.dirname(directory)+'/'+f'good_{file_name}.txt'
        with open(path,'w',encoding='utf-8')as files:
            for row in good:
                files.write(' '.join(row) + '\n')
        path = os.path.dirname(directory) + '/' + f'broke_{file_name}.txt'
        with open(path, 'w', encoding='utf-8') as files:
            for row in broke:
                files.write(' '.join(row) + '\n')
        path = os.path.dirname(directory) + '/' + f'lose_{file_name}.txt'
        with open(path, 'w', encoding='utf-8') as files:
            for row in lose:
                files.write(' '.join(row) + '\n')
        path = os.path.dirname(directory) + '/' + f'uncovered_{file_name}.txt'
        with open(path, 'w', encoding='utf-8') as files:
            for row in uncovered:
                files.write(' '.join(row) + '\n')
        path = os.path.dirname(directory) + '/' + f'circle_{file_name}.txt'
        with open(path, 'w', encoding='utf-8') as files:
            for row in circle:
                files.write(' '.join(row) + '\n')
        self.lable5.setText('文件已分类完成')

    def next(self):
        self.lable4.setText('程序正在运行中')

    def bar_bar(self,i):
        with open('path/botn_data_path1.txt','r',encoding='utf-8')as file:
            a=file.read()
        b=['.jpg','.png']
        c=len([name for name in os.listdir(a) if os.path.isfile(os.path.join(a, name)) and any(name.endswith(ext)for ext in b)])
        d=int(round(i/c,2)*100)
        self.bar.setValue(d)

    def ending(self):
        self.lable4.setText('结果已输出')
        self.btn_si.setEnabled(True)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = FileSelector()
    ex.show()
    sys.exit(app.exec_())
