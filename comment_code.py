# import os
# import re

# def comment_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#     
#     # Comment tất cả code Python
#     commented_content = re.sub(r'^(.+)$', r'# \1', content, flags=re.MULTILINE)
#     
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.write(commented_content)

# def process_directory(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.py'):
#                 file_path = os.path.join(root, file)
#                 print(f"Commenting file: {file_path}")
#                 comment_file(file_path)

# if __name__ == "__main__":
#     # Xử lý thư mục gốc
#     process_directory('.') 