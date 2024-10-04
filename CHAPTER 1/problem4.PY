import os

# Specify the directory you want to list
directory_path = '/New folder'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
