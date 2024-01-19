import os
import shutil

#定义源目录和目标目录
source_folder = "ImgData"
destination_folder = "ImgData"

#遍历源目录中所有文件
for filename in os.listdir(source_folder):
    # 确保是svs文件
    if filename.endswith(".svs"):
        # 取前12位字符
        identifier = filename[:14]

        # Create the subfolder with the identifier if it does not exist
        subfolder_path = os.path.join(destination_folder, identifier)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        # Move the file to the subfolder
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(subfolder_path, filename)
        shutil.move(src_path, dst_path)

print("已经完成所有归类！")
