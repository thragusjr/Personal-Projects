import os
import datetime

## Code logic is set to return date check on all files, therefore it is triggering folders "not up to date"
## due to older files. Need to establish list of most recent level1 and level0 files, then return whether
## those are up to date or not.

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
                # Initialize list of up-to-date directories
                up_to_date_dirs = []
                out_of_date_dirs = []
                out_of_date_files = []

                for file_name in files:
                    any_level1_up_to_date = any(is_recent_file(os.path.join(root, file_name), level1_threshold) for file_name in files)
                    any_level0_up_to_date = any(is_recent_file(os.path.join(root, file_name), level0_threshold) for file_name in files)
                    file_path = os.path.join(root, file_name)
                    if any_level0_up_to_date and any_level1_up_to_date:
                        up_to_date_dirs.append(file_path)
                    else:
                        out_of_date_dirs.append(root)
                        out_of_date_files.append(file_path)

            for directory in up_to_date_dirs:
                f.write(f"{directory} is up to date.\n")  
            
            if out_of_date_dirs:
                for directory in out_of_date_dirs:
                    f.write(f"{directory} is not up to date.\n")
            else:
                for i in out_of_date_files:
                    f.write(i + "\n")


    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: An error occurred while accessing files: {e}")


if __name__ == "__main__":
    appArray20W = ["filePath1", "filePath2", "filePath3"]
    for i in appArray20W:
        parent_directory_path = i
        output_file_path = "/home/backUp/check.txt"
        main(parent_directory_path, output_file_path)
