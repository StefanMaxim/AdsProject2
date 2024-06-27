import os

folder_path = "/path/to/your/folder"

def remove_files_from_folder(folder_path):
    files = os.listdir(folder_path)

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
