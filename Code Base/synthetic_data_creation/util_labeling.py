import os

def get_file_name_differences(folder1, folder2):
    """
    Get the file name differences (ignoring extensions) between two folders.

    Args:
        folder1 (str): Path to the first folder.
        folder2 (str): Path to the second folder.

    Returns:
        set: Set of file names (without extensions) that are in folder1 but not in folder2.
    """
    # Get the list of files (with extensions) in each folder
    files1_with_ext = set(os.listdir(folder1))
    files2_with_ext = set(os.listdir(folder2))

    # Extract file names without extensions
    files1 = {os.path.splitext(file)[0] for file in files1_with_ext}
    files2 = {os.path.splitext(file)[0] for file in files2_with_ext}

    # Return the file name differences
    return files1 - files2


# Example usage:
folder1_path = "/Path/To/ads_images_labels/kpi_real/images/"
folder2_path = "/Path/To/ads_images_labels/kpi_real/labels/"

differences1 = get_file_name_differences(folder1_path, folder2_path)
print("File name differences: folder1 vs folder2")
print(differences1)

differences2 = get_file_name_differences(folder2_path, folder1_path)
print("File name differences: folder2 vs folder1")
print(differences2)