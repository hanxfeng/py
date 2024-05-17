import os

def shanchu(file_path):
    for filename in os.listdir(file_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # 根据需要添加其他格式
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(file_path, filename)
            os.unlink(input_path)

if __name__ == '__main__':
    shanchu(r"D:\a\data\xin\broke")
    shanchu(r"D:\a\data\xin\lose")
    shanchu(r"D:\a\data\xin\good")
    shanchu(r"D:\a\data\xin\circle")
    shanchu(r"D:\a\data\xin\uncovered")