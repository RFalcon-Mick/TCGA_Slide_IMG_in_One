import os
import shutil

# 指定源目录和目标目录
source_root = "TCGA"
target_dir = "ImgData"

# 当前工作目录
current_directory = os.getcwd()

# 目标子目录的完整路径
target_full_path = os.path.join(current_directory, target_dir)
source_full_path = os.path.join(current_directory, source_root)

i = 1

# 检查ImgData目录是否存在，若不存在则创建
if not os.path.exists(target_full_path):
    os.makedirs(target_full_path)
# 检查TCGA目录是否存在，若不存在则告知
if not os.path.exists(source_full_path):
    print("请将源文件夹复制到", current_directory, "目录下！")
    os.makedirs(source_full_path)
    raise SystemExit()

# 遍历源目录下的所有子文件夹
for foldername, subfolders, filenames in os.walk(source_root):
    for filename in filenames:
        # 检查文件后缀名是否为.svs
        if filename.lower().endswith('.svs'):
            # 构建源文件的完整路径
            source_file_path = os.path.join(foldername, filename)

            # 构建目标文件的完整路径
            target_file_path = os.path.join(target_full_path, filename)

            # 复制文件
            shutil.copy2(source_file_path, target_file_path)
            print(i, f"文件 {filename} 已复制到 {target_dir} 目录下。")
            i += 1

print("所有后缀名为.svs的文件复制完毕。")
