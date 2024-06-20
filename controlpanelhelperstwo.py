from controlpanelstorage import *
from controlpanelhelpers import *
import glob
import pandas as pd

def create_complete_data_base_by_name(dictoffullschedule):
    dictoftablersschedules = dictoffullschedule
    time_ranges = timecreatorincrements()

    exportschedule = {}

    # imported dict will be {"name": object}
    for name, schedule in dictoftablersschedules.items():
        theschedule = schedule.getheschedule()

        # theschedule dict will be {"Monday": {900: "1", 915: "0"}}
        for day, dayschedule in theschedule.items():
            if day not in exportschedule:
                exportschedule[day] = {}

            # timeslots is like [900, 915, 930]
            timeslots = sorted(dayschedule.keys())
            for i in range(len(timeslots) - 1):
                if dayschedule[timeslots[i]] == "1" and dayschedule[timeslots[i + 1]] == "1":
                    if time_ranges[i] not in exportschedule[day]:
                        exportschedule[day][time_ranges[i]] = []
                    exportschedule[day][time_ranges[i]].append(name)

    return exportschedule

