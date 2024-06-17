from controlpanelstorage import *
from controlpanelhelpers import *
import glob
import pandas as pd

def main():
    dictoftablersschedules = createscheduledatabase()
    dictofdaytimes = createdaydatabase(dictoftablersschedules)
    emptyschedule = {}
    switch = True
    while switch == True:
        print("\n\nWhat would you like to do?\nAdd to the scehdeule? (A) \nQuit (Q) \nView a person's schedule(Z)")
        decision = input("\n\n")

        
        if decision.lower() == "a":
            print("What day would you like to view? \nMonday(M), \nTuesday(T), \nWednesday(W), \nThursday(Th), \nFriday(F)")
            decision = input("\n")

        elif decision.lower() == "z":
            print("Whose schedule would you like to view?")
            personsname = input("\n")
            
            if personsname.lower() in dictoftablersschedules:
                print("\nWhat day would you like to view their schedule?\nMonday(M)\nTuesday(T)\nWednesday(W)\nThursday(Th)\nFriday(F)")
                theday = input("\n")
                schedule = dictoftablersschedules[personsname.lower()].getheschedule()[theday]
                print(f"Schedule for {personsname}:")
                preparedschedule = check_consecutive_slots(schedule)
                for time, availiability in preparedschedule.items():
                    print(f"{time}: {availiability}")
            else:
                print(f"No schedule found for {personsname}.")

        elif decision.lower() == "q":
            print("Thank's for using my program!")
            exit()
            
main()


