def daysofweekstorage():
    daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return daysofweek

def daysofweekkeyconversionstorage():
    mydict = {"m": "Monday", "t": "Tuesday", "w": "Wednesday", "th": "Thursday", "f": "Friday"}
    return mydict

def timeframecreatorstorageregular():
    # Input in military time
    starttime = 900
    endtime = 1900

    timeframestoragetemp = []
    timeframesstorageexport = []
    # The time index measures how many fifteen minute increments exist between the start time and the endtime
    timeindex = ((endtime // 100) * 60 + (endtime % 100) - ((starttime // 100) * 60 + (starttime % 100))) // 15

    current_time = starttime
    for i in range(timeindex + 1):
        #Adds the military time increments to the empty list
        timeframestoragetemp.append(current_time)
        
        # Increment the time by 15 minutes in military time
        hours = current_time // 100
        minutes = current_time % 100
        minutes += 15
        if minutes == 60:
            minutes = 0
            hours += 1
        current_time = hours * 100 + minutes


    for time in timeframestoragetemp:
        hours = time // 100
        minutes = time % 100

        if hours < 12:
            period = "AM"
            formatted_time = f"{hours}:{minutes:02d} {period}"
        else:
            period = "PM"
            formatted_time = f"{hours - 12 if hours > 12 else 12}:{minutes:02d} {period}"

        timeframesstorageexport.append(formatted_time)
    
    return timeframesstorageexport



def timecreatorincrements():
    timestoragetemp = timeframecreatorstorageregular()
    timestorageexport = []
    for i in range(len(timestoragetemp) - 1):
        timestorageexport.append(f"{timestoragetemp[i]} - {timestoragetemp[i + 1]}")

    return timestorageexport



def timeframestoragemilitary():
    starttime = 900
    endtime = 1900
    timeframesstorageexport = []

    current_time = starttime
    while current_time <= endtime:
        timeframesstorageexport.append(current_time)

        # Increment the time by 15 minutes
        hours = current_time // 100
        minutes = current_time % 100
        minutes += 15

        if minutes >= 60:
            minutes -= 60
            hours += 1

        current_time = hours * 100 + minutes

    return timeframesstorageexport


def check_consecutive_slots_for_availiabilty(time_dict):
    #Right now the dictionary is an object, by using sorted, we turn it into a list
    time_slots = sorted(time_dict.keys())
    time_ranges = timecreatorincrements()

    result = {}

    for i in range(len(time_slots) - 1):
        if time_dict[time_slots[i]] == "1" and time_dict[time_slots[i + 1]] == "1":
            result[time_ranges[i]] = "availiable"
        else:
            result[time_ranges[i]] = "not availiable"

    return result
































#This function is not used yet
def militarytoregular(importeddict):
    converterdictionary = {}
    newdictionaryexport = {}
    militarytime = timeframestoragemilitary()
    regulartime = timeframecreatorstorageregular()

    for i in range(len(militarytime)):
        converterdictionary[militarytime[i]] = regulartime[i]

    #Convert the input dictionary
    #converteddictionary[keu] = "regular time" and it corresponds with the current value
    newdictionaryexport = {converterdictionary[key]: value for key, value in importeddict.items()}
    return newdictionaryexport

#Not in use yet
def oneandzero_towords(importeddict):
    converterdictionary = {"1": "availiable", "0": "not availiable"}
    newdictionaryexport = {key: converterdictionary[value] for key, value in importeddict.items()}

    return newdictionaryexport

