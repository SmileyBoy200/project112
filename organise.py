import os
import shutil

source =  "C:/Users/Matthew/Downloads" 
destination = "C:/Users/Matthew/OneDrive/Desktop"

list_of_files = os.listdir(source)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print (extension)
    print (name)
    if extension == '':
        continue
    if extension in ['.gif','.jpg','.png','.jpeg']:
        path1 = source + '/' + file_name
        path2 = destination + '/' + 'imagefiles'
        path3 = destination  + '/' + 'imagefiles' + '/' + file_name
        
        if os.path.exists (path2):
            shutil.move (path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            
    if extension in ['.exe']:
        path1 = source + '/' + file_name
        path2 = destination + '/' + 'ApplicationFiles'
        path3 = destination  + '/' + 'ApplicationFiles' + '/' + file_name
        
        if os.path.exists (path2):
            shutil.move (path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)