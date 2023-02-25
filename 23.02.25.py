import os
# print(os.getcwd())
folder = "Nado_coding"
if os.path.exists(folder):
    os.rmdir(folder)
    print(folder, "폴더가 삭제되었습니다.")
else:
    os.mkdir(folder)
    print(folder, "폴더가 생성되었습니다.")