import os
import time

folder_path = "/home/yu_deyy/Pictures"
interval_seconds = 3600  # Adjust this interval as needed (e.g., 3600 seconds = 1 hour)

while True:
    # List all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate through the files and delete them
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_name}")
            else:
                print(f"Skipped: {file_name} (not a file)")
        except Exception as e:
            print(f"Error deleting {file_name}: {str(e)}")

    print("Sleeping for {} seconds...".format(interval_seconds))
    time.sleep(interval_seconds)