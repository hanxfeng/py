import os
import shutil


# 确保目标文件夹存在
def zhuanyi(source_dir,target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_dir):
        # 构建源文件和目标文件的完整路径
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)

        # 检查是否为文件（而不是文件夹）
        if os.path.isfile(source_file):
            # 使用shutil.move()方法将文件从源路径移动到目标路径
            shutil.move(source_file, target_file)
if __name__ == '__main__':

    zhuanyi(r"D:\a\data\train\补充数据\broke",r"D:\a\data\xin\broke")