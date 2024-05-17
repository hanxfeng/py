import chardet

# 读取文件的一部分来检测编码
with open(r"D:\py\pythonProject\arima\1.csv", 'rb') as f:
    rawdata = f.read(1310)  # 读取前1000个字节通常足够检测编码
    result = chardet.detect(rawdata)

# 输出检测到的编码
print(result['encoding'])