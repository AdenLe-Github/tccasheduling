from controlpanelstorage import *
from controlpanelhelpers import *
import glob
import pandas as pd
import os

testdict = {}
testday = {}
lowertimetest = {}
uppertimetest = {}
def create_complete_data_base_by_name(dictoffullschedule):
    dictoftablersschedules = dictoffullschedule
    time_ranges = timecreatorincrements()

    exportschedule = {}

    # imported dict will be {"name": object}
    for name, schedule in dictoftablersschedules.items():
        theschedule = schedule.getheschedule()
        #print(f"{theschedule} \n\n {name} \n\n")

        # theschedule dict will be {"Monday": {900: "1", 915: "0"}}
        for day, dayschedule in theschedule.items():
            if day not in exportschedule:
                exportschedule[day] = {}
                

            # timeslots is like [900, 915, 930]
            timeslots = sorted(dayschedule.keys())
            for i in range(len(timeslots) - 1):
                if time_ranges[i] not in exportschedule[day]:
                        exportschedule[day][time_ranges[i]] = []
                if dayschedule[timeslots[i]] == "1" and dayschedule[timeslots[i + 1]] == "1":
                    exportschedule[day][time_ranges[i]].append(name)

    return exportschedule

def return_people_availiable_for_timerange(availiabitydict, theday, lowertime, uppertime):
    exportavailiability = {}


    lowervalue = lowertime
    uppervalue = uppertime

    military_time_availiability = timeframecreatorstorageregular(lowervalue, uppervalue)
    current_time_range = timecreatorincrements(military_time_availiability)


    dayrequested  = theday
    dictoftablerscheduleincrement = availiabitydict

    for i in range(len(current_time_range)):
        exportavailiability[current_time_range[i]] = (dictoftablerscheduleincrement[dayrequested][current_time_range[i]])
    print(exportavailiability)
    return exportavailiability 

def savethefile(currentschedule):
    listofdays = []
    listoftimes = []
    for day, schedule in currentschedule.items():
        listofdays.append(day)
        
        for time in schedule.keys():
            if day == "Monday":
                listoftimes.append(time)

    # Writing to the file
    with open(f"savedschedule/savedschedule1.csv", "w") as outputfile:
        # Joining elements of listofdays into a single string separated by commas
        output_header = "Time," + ",".join(listofdays) + "\n"
        outputfile.write(output_header)
        
        for time in listoftimes:
            # Writing the time slot
            people = [time]
            for day in listofdays:
                # Get the list of people for the specific day and time
                players = currentschedule[day].get(time, [])
                if players:
                    # Join the list of players into a single string separated by commas
                    people.append(" ".join(players))
                else:
                    # Add an empty field for times with no players
                    people.append("")
            
            # Join all the people (including time) into a single string separated by commas
            outputfile.write(",".join(people) + "\n")




theschedule = {'Monday': {'9:00 AM - 9:15 AM': [], '9:15 AM - 9:30 AM': [], '9:30 AM - 9:45 AM': [], '9:45 AM - 10:00 AM': [], '10:00 AM - 10:15 AM': [], '10:15 AM - 10:30 AM': [], '10:30 AM - 10:45 AM': [], '10:45 AM - 11:00 AM': [], '11:00 AM - 11:15 AM': [], '11:15 AM - 11:30 AM': [], '11:30 AM - 11:45 AM': [], '11:45 AM - 12:00 PM': [], '12:00 PM - 12:15 PM': [], '12:15 PM - 12:30 PM': [], '12:30 PM - 12:45 PM': [], '12:45 PM - 1:00 PM': [], '1:00 PM - 1:15 PM': [], '1:15 PM - 1:30 PM': [], '1:30 PM - 1:45 PM': [], '1:45 PM - 2:00 PM': [], '2:00 PM - 2:15 PM': [], '2:15 PM - 2:30 PM': [], '2:30 PM - 2:45 PM': [], '2:45 PM - 3:00 PM': [], '3:00 PM - 3:15 PM': [], '3:15 PM - 3:30 PM': [], '3:30 PM - 3:45 PM': [], '3:45 PM - 4:00 PM': [], '4:00 PM - 4:15 PM': [], '4:15 PM - 4:30 PM': [], '4:30 PM - 4:45 PM': [], '4:45 PM - 5:00 PM': [], '5:00 PM - 5:15 PM': [], '5:15 PM - 5:30 PM': [], '5:30 PM - 5:45 PM': [], '5:45 PM - 6:00 PM': [], '6:00 PM - 6:15 PM': [], '6:15 PM - 6:30 PM': [], '6:30 PM - 6:45 PM': [], '6:45 PM - 7:00 PM': []}, 'Tuesday': {'9:00 AM - 9:15 AM': [], '9:15 AM - 9:30 AM': [], '9:30 AM - 9:45 AM': [], '9:45 AM - 10:00 AM': [], '10:00 AM - 10:15 AM': ['max'], '10:15 AM - 10:30 AM': ['max'], '10:30 AM - 10:45 AM': ['max'], '10:45 AM - 11:00 AM': ['max'], '11:00 AM - 11:15 AM': ['ariel', 'max'], '11:15 AM - 11:30 AM': ['ariel', 'max'], '11:30 AM - 11:45 AM': ['ariel', 'max'], '11:45 AM - 12:00 PM': ['ariel', 'max'], '12:00 PM - 12:15 PM': [], '12:15 PM - 12:30 PM': [], '12:30 PM - 12:45 PM': [], '12:45 PM - 1:00 PM': [], '1:00 PM - 1:15 PM': [], '1:15 PM - 1:30 PM': [], '1:30 PM - 1:45 PM': [], '1:45 PM - 2:00 PM': [], '2:00 PM - 2:15 PM': [], '2:15 PM - 2:30 PM': [], '2:30 PM - 2:45 PM': [], '2:45 PM - 3:00 PM': [], '3:00 PM - 3:15 PM': [], '3:15 PM - 3:30 PM': [], '3:30 PM - 3:45 PM': [], '3:45 PM - 4:00 PM': [], '4:00 PM - 4:15 PM': [], '4:15 PM - 4:30 PM': [], '4:30 PM - 4:45 PM': [], '4:45 PM - 5:00 PM': [], '5:00 PM - 5:15 PM': [], '5:15 PM - 5:30 PM': [], '5:30 PM - 5:45 PM': [], '5:45 PM - 6:00 PM': [], '6:00 PM - 6:15 PM': [], '6:15 PM - 6:30 PM': [], '6:30 PM - 6:45 PM': [], '6:45 PM - 7:00 PM': []}, 'Wednesday': {'9:00 AM - 9:15 AM': [], '9:15 AM - 9:30 AM': [], '9:30 AM - 9:45 AM': [], '9:45 AM - 10:00 AM': [], '10:00 AM - 10:15 AM': [], '10:15 AM - 10:30 AM': [], '10:30 AM - 10:45 AM': [], '10:45 AM - 11:00 AM': [], '11:00 AM - 11:15 AM': [], '11:15 AM - 11:30 AM': [], '11:30 AM - 11:45 AM': [], '11:45 AM - 12:00 PM': [], '12:00 PM - 12:15 PM': [], '12:15 PM - 12:30 PM': [], '12:30 PM - 12:45 PM': [], '12:45 PM - 1:00 PM': [], '1:00 PM - 1:15 PM': [], '1:15 PM - 1:30 PM': [], '1:30 PM - 1:45 PM': [], '1:45 PM - 2:00 PM': [], '2:00 PM - 2:15 PM': [], '2:15 PM - 2:30 PM': [], '2:30 PM - 2:45 PM': [], '2:45 PM - 3:00 PM': [], '3:00 PM - 3:15 PM': [], '3:15 PM - 3:30 PM': [], '3:30 PM - 3:45 PM': [], '3:45 PM - 4:00 PM': [], '4:00 PM - 4:15 PM': [], '4:15 PM - 4:30 PM': [], '4:30 PM - 4:45 PM': [], '4:45 PM - 5:00 PM': [], '5:00 PM - 5:15 PM': [], '5:15 PM - 5:30 PM': [], '5:30 PM - 5:45 PM': [], '5:45 PM - 6:00 PM': [], '6:00 PM - 6:15 PM': [], '6:15 PM - 6:30 PM': [], '6:30 PM - 6:45 PM': [], '6:45 PM - 7:00 PM': []}, 'Thursday': {'9:00 AM - 9:15 AM': [], '9:15 AM - 9:30 AM': [], '9:30 AM - 9:45 AM': [], '9:45 AM - 10:00 AM': [], '10:00 AM - 10:15 AM': [], '10:15 AM - 10:30 AM': [], '10:30 AM - 10:45 AM': [], '10:45 AM - 11:00 AM': [], '11:00 AM - 11:15 AM': [], '11:15 AM - 11:30 AM': [], '11:30 AM - 11:45 AM': [], '11:45 AM - 12:00 PM': [], '12:00 PM - 12:15 PM': [], '12:15 PM - 12:30 PM': [], '12:30 PM - 12:45 PM': [], '12:45 PM - 1:00 PM': [], '1:00 PM - 1:15 PM': [], '1:15 PM - 1:30 PM': [], '1:30 PM - 1:45 PM': [], '1:45 PM - 2:00 PM': [], '2:00 PM - 2:15 PM': [], '2:15 PM - 2:30 PM': [], '2:30 PM - 2:45 PM': [], '2:45 PM - 3:00 PM': [], '3:00 PM - 3:15 PM': [], '3:15 PM - 3:30 PM': [], '3:30 PM - 3:45 PM': [], '3:45 PM - 4:00 PM': [], '4:00 PM - 4:15 PM': [], '4:15 PM - 4:30 PM': [], '4:30 PM - 4:45 PM': [], '4:45 PM - 5:00 PM': [], '5:00 PM - 5:15 PM': [], '5:15 PM - 5:30 PM': [], '5:30 PM - 5:45 PM': [], '5:45 PM - 6:00 PM': [], '6:00 PM - 6:15 PM': [], '6:15 PM - 6:30 PM': [], '6:30 PM - 6:45 PM': [], '6:45 PM - 7:00 PM': []}, 'Friday': {'9:00 AM - 9:15 AM': [], '9:15 AM - 9:30 AM': [], '9:30 AM - 9:45 AM': [], '9:45 AM - 10:00 AM': [], '10:00 AM - 10:15 AM': [], '10:15 AM - 10:30 AM': [], '10:30 AM - 10:45 AM': [], '10:45 AM - 11:00 AM': [], '11:00 AM - 11:15 AM': [], '11:15 AM - 11:30 AM': [], '11:30 AM - 11:45 AM': [], '11:45 AM - 12:00 PM': [], '12:00 PM - 12:15 PM': [], '12:15 PM - 12:30 PM': [], '12:30 PM - 12:45 PM': [], '12:45 PM - 1:00 PM': [], '1:00 PM - 1:15 PM': [], '1:15 PM - 1:30 PM': [], '1:30 PM - 1:45 PM': [], '1:45 PM - 2:00 PM': [], '2:00 PM - 2:15 PM': [], '2:15 PM - 2:30 PM': [], '2:30 PM - 2:45 PM': [], '2:45 PM - 3:00 PM': [], '3:00 PM - 3:15 PM': [], '3:15 PM - 3:30 PM': [], '3:30 PM - 3:45 PM': [], '3:45 PM - 4:00 PM': [], '4:00 PM - 4:15 PM': [], '4:15 PM - 4:30 PM': [], '4:30 PM - 4:45 PM': [], '4:45 PM - 5:00 PM': [], '5:00 PM - 5:15 PM': [], '5:15 PM - 5:30 PM': [], '5:30 PM - 5:45 PM': [], '5:45 PM - 6:00 PM': [], '6:00 PM - 6:15 PM': [], '6:15 PM - 6:30 PM': [], '6:30 PM - 6:45 PM': [], '6:45 PM - 7:00 PM': []}}
savethefile(theschedule)