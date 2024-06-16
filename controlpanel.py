from controlpanelstorage import *
from controlpanelhelpers import *

class Tablers:

    def __init__(self, schedule):
        self.__schedule = schedule

    def viewtheschedule(self):
        return self.__schedule


def main():
    switch = True

    listoftablers = {}

    while switch == True:
        print("What would you like to do?\nAdd a tabler? (A) \nQuit (Q) \nView a person's schedule(Z)")
        decision = input("\n\n")


        if decision.lower() == "a":
            filename, personsname = retrieve_file_helper()
            schedule = extract_schedule_helper(filename)
            print(schedule)
            tabler = Tablers(schedule)
            print("test")
            listoftablers[personsname] = tabler
            print(listoftablers)

        elif decision.lower() == "z":
            print("Whose schedule would you like to view?")
            personsname = input("\n")
            
            if personsname in listoftablers:
                schedule = listoftablers[personsname].viewtheschedule()
                print(f"Schedule for {personsname}:")
                print(schedule)
            else:
                print(f"No schedule found for {personsname}.")


        elif decision.lower() == "q":
            print("Thank's for using my program!")
            exit()




main()