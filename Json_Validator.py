# This program will auto-validate the JSON file submitted by the technician
# and then create a PDF file once it's confirmed that it is a valid JSON file.
# Created by Antonio Vargas (AV6835)

import CreateDirectories  # importing the create_directories function
import Menu  # importing the menu

# When user starts the program, I want to check if the JSON_TO_PDF directory already exists
# If the directory does not exist then create it and open the directory window.
CreateDirectories.create_directories()

# After the directories have been created or validated then I want to ask the user some information
# about the JSON file. First I'd like to know the CLO number.

# Start the Menu
Menu.menu()