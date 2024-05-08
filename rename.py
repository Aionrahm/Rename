import os
import shutil
import time


def rename_file(files):
    files.remove("rename.py")
    for f in files:

    # Destination file path
        new_file_name = file_create_date(f) + f
        print(new_file_name)
    # Check if the source file exists
        if os.path.exists(f):
            # Rename the file
            shutil.move(f, new_file_name)
            print("File renamed successfully.")
        else:
            print("Source file does not exist.")

def get_file_names():
    # Folder path
    folder_path = os.getcwd()
    # Get the list of files in the folder
    return os.listdir(folder_path)

def file_create_date(path):
    return time.strftime("%H%M_", time.localtime(os.path.getctime(path)))

files = get_file_names()
rename_file(files)