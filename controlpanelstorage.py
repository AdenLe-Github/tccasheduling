def daysofweekstorage():
    daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return daysofweek

def timeframecreatorstorage():
    #Input in military time
    starttime = 900
    endtime = 1900

    timeframestoragetemp = []
    timeframesstorageexport = []
    #The time index measures how many fifteen minute increments that exist between the start time and the endtime
    timeindex = (endtime - starttime) // 25

    for i in range (timeindex + 1):
        if i != 0:
            if ((starttime + 15) % 100) == 60:
                starttime -= 45
                starttime += 100

            else: 
                starttime += 15

        timeframestoragetemp.append(starttime)

    for i in timeframestoragetemp:
        timeholder = i

        if timeholder < 1200:
            timeholder = str(timeholder)

            if len(timeholder) == 3:
                formattedtime = (f"{timeholder[0]}:{timeholder[1:]} AM")

            elif len(timeholder) == 4:
                formattedtime = (f"{timeholder[0:2]}:{timeholder[2:]} AM")

        elif timeholder >= 1200:
            timeholder = str(timeholder - 1000)
            if len(timeholder) == 3:
                formattedtime = (f"{timeholder[0]}:{timeholder[1:]} PM")

            elif len(timeholder) == 4:
                formattedtime = (f"{timeholder[0:2]}:{timeholder[2:]} PM")

        timeframesstorageexport.append(formattedtime)
        
    return timeframesstorageexport
