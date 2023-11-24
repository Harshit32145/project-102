import os
import shutil
import time

source = "C:/Users/harsh/Downloads"
destination = "C:/Users/harsh/OneDrive/Desktop/Projects/project 102"

list_of_files = os.listdir(source)

#print(list_of_files)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    #print(name)
    #print(ext)

    if ext =="":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1 = source+"/"+file
        path2 = destination+"/"+"documents_files"
        path3 = destination+"/"+"documents_files"+"/"+file

        if os.path.exists(path2):
            time.sleep(1)
            print("moving the file"+file)
            shutil.move(path1,path3)
        else:
            time.sleep(1)
            print("creating the path")
            os.makedirs(path2)

            print("moving the file"+file)
            shutil.move(path1,path3)
