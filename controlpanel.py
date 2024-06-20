from controlpanelstorage import *
from controlpanelhelpers import *
from controlpanelhelperstwo import *
import glob
import pandas as pd

def main():

    #main tool
    dictoftablersschedules = createscheduledatabase()
    dictoftablerscheduleincrement = create_complete_data_base_by_name(dictoftablersschedules)

    #{"m": "Monday"}
    dayacronymcoversion = daysofweekkeyconversionstorage()
    emptyschedule = {}
    switch = True
    while switch == True:
        print("\n\nWhat would you like to do?\nView who is availiable for what time, per day (A) \nQuit (Q) \nView a person's schedule(Z)")
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
            
main()


