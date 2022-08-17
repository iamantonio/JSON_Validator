# I want to create the directories for importing JSON files
# importing the os module
import os
import time

# directories
main_directory = "JSON_TO_PDF"
import_directory = "IMPORT_JSON_FILE_HERE"
export_directory = "JSON_PDF_EXPORTED_HERE"
invalid_directory = "INVALID_JSON_FILES"

# parent directory path
parent_directory = os.path.expanduser('~')

# create paths
main_path = os.path.join(parent_directory, main_directory)
import_path = os.path.join(main_path, import_directory)
export_path = os.path.join(main_path, export_directory)
invalid_path = os.path.join(main_path, invalid_directory)


def create_directories():
    # check if directory exists
    directory_exists = os.path.isdir(main_path)
    if directory_exists:
        print("Directory '% s' exists!" % main_directory)
        print("Continuing to the main menu....")
    else:
        # create the main directory and subdirectories if main directory doesn't exist
        os.mkdir(main_path)
        os.mkdir(import_path)
        os.mkdir(export_path)
        os.mkdir(invalid_path)
        print("Directory '% s' created" % main_directory)
        print("Continuing to the main menu....")
        time.sleep(2)
