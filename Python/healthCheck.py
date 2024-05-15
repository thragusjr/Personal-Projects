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

    # Get the modification time of the file
    modification_time = os.path.getmtime(file_path)
    file_age = (datetime.datetime.today() - datetime.datetime.fromtimestamp(modification_time)).days

    return file_age < age_threshold_in_days


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
            # Iterate through files
            for root, dirs, files in os.walk(parent_directory):
                # Check if files are up-to-date
                all_files_up_to_date = all(is_recent_file(os.path.join(root, file_name), level1_threshold if "level1" in file_name else level0_threshold) for file_name in files)
                # Initialize list of up-to-date directories
                up_to_date_dirs = []
                if all_files_up_to_date:
                    up_to_date_dirs.append(root)
                for directory in dirs:
                    dir_path = os.path.join(root, directory)
                    if all(is_recent_file(os.path.join(dir_path, file_name), level1_threshold if "level1" in file_name else level0_threshold) for file_name in os.listdir(dir_path)):
                        up_to_date_dirs.append(dir_path)
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    if is_recent_file(file_path, level1_threshold if "level1" in file_name else level0_threshold):
                        f.write(f"{file_name} in {root} is up to date.\n")
                    else:
                        f.write(f"WARNING {file_name} in {root} is not up to date.\n")

            for directory in up_to_date_dirs:
                f.write(f"{directory} is up to date.\n")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: An error occurred while accessing files: {e}")


if __name__ == "__main__":
    parent_directory_path = "/"
    output_file_path = "/home/Documents/health-check.txt"
    main(parent_directory_path, output_file_path)
