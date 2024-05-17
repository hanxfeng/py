import os

def duqu(path):
    b=[]
    for root, dirs, files in os.walk(path):
        for file_name in files:
            a=f"{os.path.join(root, file_name)}"
            b.append(a)
    return b




