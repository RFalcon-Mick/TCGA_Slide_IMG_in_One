import os
import shutil

# 文件夹名称
folders_to_check = ['ImgData', 'TCGA']

# 检查并创建文件夹
for folder in folders_to_check:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"已创建文件夹: {folder}")
    else:
        print(f"文件夹已存在: {folder}")
