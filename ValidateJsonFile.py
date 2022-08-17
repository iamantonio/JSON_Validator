# What do I want to do here??
# I want to validate the JSON files

import webbrowser
import os
import CreateDirectories
import json
import time
import Menu
from fpdf import FPDF
import shutil


def is_dir_empty():
    list_directory = os.listdir(CreateDirectories.import_path)
    if len(list_directory) == 0:
        print("No files found in", CreateDirectories.import_path)
        print("Move JSON file to directory and try again")
        print("Opening the directory now and returning to main menu...")
        time.sleep(4)
        webbrowser.open(CreateDirectories.import_path)


def thresholds():
    print("Tech will need to adjust threshold and resubmit new JSON file.")
    os.system("pause")
    Menu.menu()


def open_dark_fiber_ticket():
    # URL to the dark fiber ticket tool
    dark_fiber_ticket = input("\tEnter the Dark Fiber Ticket Number: ")
    dark_fiber_tool_URL = "https://gfso.web.att.com/DarkFiber/req-edit.php?id=" + dark_fiber_ticket
    webbrowser.open(dark_fiber_tool_URL)


def validate_file():
    os.system("CLS")

    # Let's get some information about the JSON file
    is_dir_empty()

    for file in os.listdir(CreateDirectories.import_path):
        if file.endswith(".json"):
            print(f'\nValidating {file}....')
            x = os.path.join(CreateDirectories.import_path, file)
            with open(x, 'r') as f:
                data = json.load(f)
            spliceLossThreshold = data['Label']['spliceLossThreshold']
            connectorLossThreshold = data['Label']['connectorLossThreshold']
            eventReflectanceThreshold = data['Label']['eventReflectanceThreshold']
            strandOrlThreshold = data['Label']['strandOrlThreshold']
            cableId = data['Label']['cableId']
            tested = data['Label']['Tested']

            print("-------------------------------------")
            print("| Fiber Cable ID: \t\t", cableId)
            print("-------------------------------------")

            # for loop to check each strand inside the Tested section of JSON
            for strands in tested:
                strand = strands['strand']
                passFail = strands['passFail']

                if passFail != "pass":
                    print("\nStrand", strand, "did not pass test!\n")
                    print("Tech will need to retest and resubmit new JSON file.")
                    print("Exiting program")
                    time.sleep(2)
                    exit(0)
                    break
                else:
                    print("Strand: \t\t\t", strand)
                    print("Pass / Fail: \t\t\t", passFail)

            if spliceLossThreshold != 0.5:
                print("\nSplice Loss Threshold is not properly set!")
                print("Should be set to 0.5 not", spliceLossThreshold, "\n")
                thresholds()
            else:
                print("Splice Loss Threshold:\t\t", spliceLossThreshold)

            if connectorLossThreshold != 0.99:
                print("\nConnector Loss Threshold is not properly set!")
                print("Should be set to 0.99 not", connectorLossThreshold, "\n")
                thresholds()
            else:
                print("Connector Loss Threshold:\t", connectorLossThreshold)

            if eventReflectanceThreshold != -40.0:
                print("\nEvent Reflectance Threshold is not properly set!")
                print("Should be set to -40.0 not", eventReflectanceThreshold, "\n")
                thresholds()
            else:
                print("Event Reflectance Threshold:", eventReflectanceThreshold)

            if strandOrlThreshold != 28.0:
                print("\nStrand ORL Threshold is not properly set!")
                print("Should be set to 28.0 not", strandOrlThreshold, "\n")
                thresholds()
            else:
                print("Strand ORL Threshold:\t\t", strandOrlThreshold)

            if spliceLossThreshold == 0.5 and connectorLossThreshold == 0.99 and eventReflectanceThreshold == -40.0 and strandOrlThreshold == 28.0:
                # I need to convert the json file to txt before converting it to a pdf file
                # Steps to remove ext from file
                base_file = os.path.basename(x)
                file_without_ext = os.path.splitext(base_file)[0]

                # convert json to txt
                with open(file_without_ext + ".txt", 'w') as outfile:
                    json.dump(data, outfile, indent=1)

                # convert txt to pdf
                pdf = FPDF()

                # add a page
                pdf.add_page()

                # setting styles and size of font
                pdf.set_font("Arial", size=11)

                txt_file = open(file_without_ext + ".txt", "r")

                for i in txt_file:
                    pdf.cell(100, 6, txt=i, ln=1, align="L")

                pdf.output(CreateDirectories.export_path + "\\" + file_without_ext + ".pdf")
                txt_file.close()
                f.close()
                os.remove(file_without_ext+".txt")
                shutil.move(x, CreateDirectories.export_path)

        os.system("pause")