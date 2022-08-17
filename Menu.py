import time
import os
import ValidateJsonFile
import JsonViewer
import sys


def menu():
    user_choice = 0
    while user_choice != 4:
        os.system("cls")
        print("\t\t------------------------------------")
        print("\t\t|                                  |")
        print("\t\t|          JSON to PDF             |")
        print("\t\t|      1. JSON Auto Validator      |")
        print("\t\t|      2. View JSON File           |")
        print("\t\t|      3. View Dark Fiber Ticket   |")
        print("\t\t|      4. Quit Program             |")
        print("\t\t|                                  |")
        print("\t\t------------------------------------")

        try:
            user_choice = int(input("\tEnter your option: "))
            if user_choice == 1:
                ValidateJsonFile.validate_file()
            elif user_choice == 2:
                JsonViewer.view_json()
            elif user_choice == 3:
                ValidateJsonFile.open_dark_fiber_ticket()
            elif user_choice == 4:
                print("\tQuitting the program")
                time.sleep(1.3)
                sys.exit(0)
            else:
                print("You did not pick a valid option, try again!")
                time.sleep(2)
        except ValueError:
            print("Please enter a number only...")
            time.sleep(2)

