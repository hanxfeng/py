import os

# 设置你的目录# 替换为你的目录路径
def ming(directory):
    # 获取目录中的所有文件
    files = os.listdir(directory)

    # 初始化计数器
    count = 1

    # 遍历文件并重命名
    for file in files:
        # 检查文件是否以.jpg结尾
        if file.endswith('.jpg'):
            # 构建新的文件名
            new_file_name = f'u{count}.jpg'
            # 构建旧文件和新文件的完整路径
            old_file = os.path.join(directory, file)
            new_file = os.path.join(directory, new_file_name)
            # 重命名文件
            if not os.path.exists(new_file):
                # 重命名文件
                os.rename(old_file, new_file)
                # 打印重命名后的文件名（可选）
                print(f'Renamed {file} to {new_file_name}')
            else:
                 # 如果新文件名已存在，则打印消息并跳过
                #print(f'Skipping {file} because {new_file_name} already exists.')
                new_nam=f'new_na_{count}.jpg'
                new_file =os.path.join(directory, new_nam)
                os.rename(old_file, new_file)
                print("文件已重命名")
            count += 1

def ming2(directory):
    # 获取目录中的所有文件
    files = os.listdir(directory)

    # 初始化计数器
    count = 1

    # 遍历文件并重命名
    for file in files:
        # 检查文件是否以.jpg结尾
        if file.endswith('.jpg'):
            # 构建新的文件名
            new_file_name = f'name_{count}.jpg'
            # 构建旧文件和新文件的完整路径
            old_file = os.path.join(directory, file)
            new_file = os.path.join(directory, new_file_name)
            # 重命名文件
            if not os.path.exists(new_file):
                # 重命名文件
                os.rename(old_file, new_file)
                # 打印重命名后的文件名（可选）
                print(f'Renamed {file} to {new_file_name}')
            else:
                # 如果新文件名已存在，则打印消息并跳过
                print(f'Skipping {file} because {new_file_name} already exists.')
            count += 1

if __name__ == '__main__':

    ming(r'D:\a\csv')