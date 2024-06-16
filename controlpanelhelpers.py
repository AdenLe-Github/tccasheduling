import os
from controlpanelstorage import *

def check_file_in_folder_helper(folder, filename):
    #Checks within folders
    full_path = os.path.join(folder, filename)
    #returns the full_path of the file
    print(full_path)
    return os.path.isfile(full_path), full_path

def retrieve_file_helper():
    # Used to retrieve the mRNA file if it exists and the folder_path is correct
    print("\n\n")

    # If the inputcode or the mrnatranscript file have been altered, the folder_path must be changed
    folder_path = "schedules/"
    print("What is the name of the Officer/JO of interest?")
    personsname = input("\n\n")
    print("Input the filename containing the officer's schedule, make sure to include the \nfile type in the end, (ex: filename.csv): ")
    print("\n\n")
    file_name = input("")

    file_exists = check_file_in_folder_helper(folder_path, file_name)
    print(f"File '{file_name}' exists: {file_exists[0]}")

    while not file_exists[0]:
        print("The file does not exist")
        user_decision = input("Would you like to quit (N) or input a different file? (Y): ")
        if user_decision.lower() == "n":
            print("Thank you for using my program, have a good day!")
            exit()
        elif user_decision.lower() == "y":
            print("Input the filename containing the officer's schedule, make sure to include the \nfile type in the end, (ex: filename.csv): ")
            file_name = input("")
            file_exists = check_file_in_folder_helper(folder_path, file_name)
            print(f"File '{file_name}' exists: {file_exists[0]}")
        else:
            print("Command was not recognized, try again")

    return file_exists[1], personsname


def extract_schedule_helper(filename):
    #Open's the file
    daysofweek = daysofweekstorage()
    skippingindex = len(daysofweek)
    
    #Creates a dictionary with keys as days of the week, each with an empty dictionary
    #Basically dictionaries within dictionaries
    weekschedule = {day: {} for day in daysofweek}


    with open(filename, "r") as insidefile:
        for line in insidefile:

            newtext = line
            #Skips lines that do not have the 
            if newtext[0].isnumeric() == False:
                continue

            else:
                for i in range(skippingindex + 1):
                    if i == 0: 
                        splicingindex = newtext.find(",")
                        time = newtext[:splicingindex]
                        newtext = newtext[splicingindex + 1:]

                    else:
                        splicingindex = newtext.find(",")
                        weekschedule[daysofweek[i - 1]][time] = newtext[:splicingindex]
                        newtext = newtext[splicingindex + 1:]
        return weekschedule
                    
