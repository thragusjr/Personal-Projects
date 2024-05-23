import os
import datetime

def is_recent_file(file_path, age_threshold_in_days):
    """
    Checks if a file is considered recent based on its modification time and a threshold.

    Args:
        file_path (str): Path to the file.
        age_threshold_in_days (int): Maximum age (in days) for a file to be considered recent.

    Returns:
        bool: True if the file is younger than the threshold, False otherwise.
    """
    try:
        # Get the modification time of the file
        modification_time = os.path.getmtime(file_path)
        file_age = (datetime.datetime.today() - datetime.datetime.fromtimestamp(modification_time)).days
        return file_age < age_threshold_in_days
    except FileNotFoundError:
        return False

def main(parent_directory, output_file, level1_threshold=1, level0_threshold=14):
    """
    Checks for up-to-date files and directories within a directory structure and writes a report.

    Args:
        parent_directory (str): Path to the parent directory to start searching.
        output_file (str): Path to the file where the report will be written.
        level1_threshold (int, optional): Maximum age (in days) for "level1" files to be considered recent. Defaults to 1.
        level0_threshold (int, optional): Maximum age (in days) for "level0" files to be considered recent. Defaults to 14.
    """
    try:
        # Open file to write to
        with open(output_file, "w") as f:
            for root, dirs, files in os.walk(parent_directory):
                any_level1_up_to_date = False
                any_level0_up_to_date = False

                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    if is_recent_file(file_path, level1_threshold):
                        any_level1_up_to_date = True
                    if is_recent_file(file_path, level0_threshold):
                        any_level0_up_to_date = True

                if any_level0_up_to_date and any_level1_up_to_date:
                    f.write(f"{root} is up to date.\n")
                else:
                    f.write(f"{root} is not up to date.\n")
                    for file_name in files:
                        file_path = os.path.join(root, file_name)
                        f.write(f"{file_path} is not up to date.\n")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: An error occurred while accessing files: {e}")

if __name__ == "__main__":
    appArray20W = ["filePath1", "filePath2", "filePath3"]
    for i in appArray20W:
        parent_directory_path = i
        output_file_path = "/home/backUp/check.txt"
        main(parent_directory_path, output_file_path)
