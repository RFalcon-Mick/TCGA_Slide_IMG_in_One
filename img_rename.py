import os

# 确认 'ImgData' 目录存在
if not os.path.exists('ImgData'):
    raise ValueError("'ImgData' 目录不存在")

# 遍历 'ImgData' 目录
for root, _, files in os.walk('ImgData'):
    for file in files:
        # 只处理 .svs 文件
        if file.endswith('.svs'):
            # 获取文件的完整路径
            file_path = os.path.join(root, file)

            # 获取文件名的前19个字符
            name_19chars = file[:23]

            # 构造新文件名
            new_name = name_19chars + '.svs'

            # 重命名文件
            new_file_path = os.path.join(root, new_name)
            os.rename(file_path, new_file_path)

            print(f"重命名文件 {file_path} 为 {new_file_path}")
