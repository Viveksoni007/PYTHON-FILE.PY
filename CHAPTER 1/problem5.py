import os
# select the path of directary content whose want to list file 
directory_path = '/'
contents = os.listdir(directory_path)
# use the os module to list the directory_path or contrent
for item in contents:
    print(item)
