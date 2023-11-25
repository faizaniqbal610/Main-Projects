import os
import shutil

video_path = 'C:\\Users\\faiza\\Downloads\\Video'
video = os.listdir(video_path)
os.chdir('C:\\Users\\faiza\\Downloads\\Video')

folderName = input("Folder name: ")
file = input("Word in file name: ")

if not os.path.exists(folderName):
    os.mkdir(folderName)

for i in video:
    if file in i.lower():
        print(f"[{i.lower()}]\n")
        shutil.move(i, folderName)

