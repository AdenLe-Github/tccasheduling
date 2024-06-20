import os
from controlpanelstorage import *
import glob
import pandas as pd

class Tablers:
    #Creates a class for each person which contains the dictionary of each of their schedules

    def __init__(self, schedule):
        self.__schedule = schedule

    def getheschedule(self):
        return self.__schedule

def retrieve_file_helper():
    #Retrieves a list of all of the CSV files in the folder schedules
        # Specify the folder containing the CSV files
    folder_path = 'schedules'  # Replace with your folder path

    # Get all CSV files in the folder and puts them in a list
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    #Returns it as a list
    return csv_files


def extract_schedule_helper(filename):
    #Open's the file, only one file at a time so it will run x times for the x amount of files

    #Returns a list with each day of the week
    daysofweek = daysofweekstorage()
    #Returns a list of all the military times within the given range
    timestorage = timeframestoragemilitary()

    #Used for downstream applications
    count = 0
    
    #Creates a dictionary with keys as days of the week, each with an empty dictionary
    #Basically dictionaries within dictionaries
    weekschedule = {day: {} for day in daysofweek}


    with open(filename, "r") as insidefile:
        #Reads each of the lines
        for line in insidefile:

            newtext = line
            
            #Isolates the line with the name with it 
            if "Name:" in newtext:
                splicingindex = newtext.find("Name:")
                newtext = newtext[splicingindex + 6:]
                splicingindex = newtext.find(",")
                #Extracts the tabler's name
                personsname = newtext[:splicingindex]
                
            #Skips all lines that don't start with a time
            elif newtext[0].isnumeric() == False:
                continue

            else:
                splicingindex = newtext.find(",")
                newtext = newtext[splicingindex + 1:]
                for day in daysofweek:
                    #Add's the times in for each day of the week
                    splicingindex = newtext.find(",")
                    weekschedule[day][timestorage[count]] = newtext[:splicingindex]
                    newtext = newtext[splicingindex + 1:]

                count += 1
        #Return's the person;s schedule under standard time and their name
        return weekschedule,personsname
    
def createscheduledatabase():
    dictoftablers = {}
    
    #Uses the function to get the list of all availiable csv files
    listoffiles = retrieve_file_helper()
    for file in listoffiles:
        #Extracts the information from each of the file
        schedule, personsname = extract_schedule_helper(file)
        personsname = personsname.lower()
        #Creates a class for each of the schedule
        tabler = Tablers(schedule)
        #Stores this in a dictionary
        dictoftablers[personsname] = tabler

    return dictoftablers

def createdaydatabase(scheduledict): #Schedule dict is the dictionary of everyone's schedule
    #This command will create the data base in which we will se who is availiable for each day of the week
    counter = 0

    #Gives me a list of the days of the week that we are looking at
    daysofweek = daysofweekstorage()

    timeframe = timeframestoragemilitary()

    #Gives me a list of the times that we are looking at
    daydatabase = {}

    #Creates the dictionary where each day and time will have a person's name in it
    daydatabase = {day: {time: [] for time in timeframe} for day in daysofweek}

    # Populate the day database based on each person's schedule
    for name, schedule in scheduledict.items():
        person_schedule = schedule.getheschedule()
        for day in daysofweek:
            for time, available in person_schedule[day].items():

                #Adds there name to the database
                if available == "1":
                    daydatabase[day][time].append(name)
        
    return daydatabase





























"""def retrieve_file_helper():
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


def check_file_in_folder_helper(folder, filename):
    #Checks within folders
    full_path = os.path.join(folder, filename)
    #returns the full_path of the file
    print(full_path)
    return os.path.isfile(full_path), full_path
"""