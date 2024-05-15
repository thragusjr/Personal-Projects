import os
import datetime

def is_recent_file(file_path):
    # Get the birth time of the file
    file_stat = os.stat(file_path)
    birth_time = datetime.datetime.fromtimestamp(file_stat.st_birthtime).date()
    
    # Get the current time
    current_time = datetime.date.today()
    
    # Calculate the difference between current time and birth time of the file
    delta = current_time - birth_time
    
    # Check if incrementals are less than a day old
    if "level1" in file_path:
        return delta.days < 1
    # Check if fulls are less than two weeks old
    elif "level0" in file_path:
        return delta.days < 15
    # For files not matching, consider them older than two weeks
    else:
        return False

def main(parent_directory, output_file):
    all_files_up_to_date = all(is_recent_file(os.path.join(root, file_name)) for file_name in files)
    up_to_date_dirs=[]
    if all_files_up_to_date:
        up_to_date_dirs.add(root)

    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(parent_directory):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                if all(is_recent_file(os.path.join(dir_path, file_name)) for file_name in os.listdir(dir_path)):
                    up_to_date_dirs.add(dir_path)
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if is_recent_file(file_path):
                    if "level1" in file_name:
                        f.write(f"{file_name} in {root} is up to date.\n")
                    elif "level0" in file_name:
                        f.write(f"{file_name} in {root} is up to date.\n")
                else:
                    f.write(f"WARNING {file_name} in {root} is not up to date.\n")
        
        for directory in up_to_date_dirs:
            f.write(f"{directory} is up to date.\n")

if __name__ == "__main__":
    parent_directory_path = "/arbor-backups"
    output_file_path = "/home/epage/Documents/health-check.txt"
    main(parent_directory_path, output_file_path)
