from controlpanelstorage import *
from controlpanelhelpers import *
from controlpanelhelperstwo import *
import glob
import pandas as pd

def main():

    #main tool
    dictoftablersschedules = createscheduledatabase()
    dictoftablerscheduleincrement = create_complete_data_base_by_name(dictoftablersschedules)
    current_schedule = {}
    increments = timecreatorincrements()

    for day in daysofweekstorage():
        current_schedule[day] = {}
        for timeincrements in increments:
            current_schedule[day][timeincrements] = []

    #{"m": "Monday"}
    dayacronymcoversion = daysofweekkeyconversionstorage()



    switch = True
    while switch == True:
        print("\n\nWhat would you like to do?\nView who is availiable for what time, per day (A)\n Schedule someone (B)\nSave the schedule \nQuit (Q) \nView a person's schedule(Z)")
        decision = input("\n\n")

        
        if decision.lower() == "a":
            print("What day would you like to view? \nMonday(M), \nTuesday(T), \nWednesday(W), \nThursday(Th), \nFriday(F)")
            theday = dayacronymcoversion[input("\n").lower()]
            print(f"Schedule for {theday}:")
            for time, availiability in dictoftablerscheduleincrement[theday].items():
                mystring = ""
                for i in range(len(availiability)):
                    mystring = (f"{mystring} {availiability[i]}")
                print(f"{time}: {mystring}")

        if decision.lower() == "b":
            print("What day would you like to schedule someone\nMonday(M), \nTuesday(T), \nWednesday(W), \nThursday(Th), \nFriday(F)?")
            theday = dayacronymcoversion[input("\n").lower()]
            print("What time would you like to see the availiabilty for?")
            print("\nEnter Lowerbound in Military Time")
            lowerbound = input("\n")
            print("\nEnter Upperbound in Military Time")
            upperbound = input("\n")
            current_time_availiabilty = return_people_availiable_for_timerange(dictoftablerscheduleincrement, theday, lowerbound, upperbound)
            for time, availiability in current_time_availiabilty.items():
                mystring = ""
                for i in range(len(availiability)):
                    mystring = (f"{mystring} {availiability[i]}")
                print(f"{time}: {mystring}")

            print("Who would you like to schedule for this time?")
            name = input("")
            for time in current_time_availiabilty:
                current_schedule[theday][time].append(name)

            print(f"The new schedule for {theday} is:")
            for time, availiability in current_schedule[theday].items():
                mystring = ""
                for i in range(len(availiability)):
                    mystring = (f"{mystring} {availiability[i]}")
                print(f"{time}: {mystring}")       

        elif decision.lower() == "z":
            print("Whose schedule would you like to view?")
            personsname = input("\n")
            
            if personsname.lower() in dictoftablersschedules:
                print("\nWhat day would you like to view their schedule?\nMonday(M)\nTuesday(T)\nWednesday(W)\nThursday(Th)\nFriday(F)")
                theday = dayacronymcoversion[input("\n").lower()]
                schedule = dictoftablersschedules[personsname.lower()].getheschedule()[theday]
                print(f"Schedule for {personsname}:")
                preparedschedule = check_consecutive_slots_for_availiabilty(schedule)
                for time, availiability in preparedschedule.items():
                    print(f"{time}: {availiability}")
            else:
                print(f"No schedule found for {personsname}.")

        elif decision.lower() == "q":
            print("Thank's for using my program!")
            exit()
            

        elif decision.lower() == "s":
            print(current_schedule)
            print("The file has now been saved")
            with open(f"savedschedule/savedschedule1.txt", "w") as outputfile:
                for day in current_schedule.keys():
                    outputfile.write(f"{day}", end="")
main()


