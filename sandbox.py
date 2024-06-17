def generate_time_ranges(time_slots):
    """
    Generates time ranges in the format "9:00 AM - 9:15 AM" from a list of military time slots.
    """
    regular_times = timeframecreatorstorageregular(time_slots)
    time_ranges = []

    for i in range(len(regular_times) - 1):
        start_time = regular_times[i]
        end_time = regular_times[i + 1]
        time_ranges.append(f"{start_time} - {end_time}")

    return time_ranges

def timeframecreatorstorageregular(time_slots):
    """
    Converts a list of military time slots to regular time format.
    """
    regular_times = []

    for time in time_slots:
        hours = time // 100
        minutes = time % 100

        if hours < 12:
            period = "AM"
            formatted_time = f"{hours}:{minutes:02d} {period}"
        else:
            period = "PM"
            formatted_time = f"{hours - 12 if hours > 12 else 12}:{minutes:02d} {period}"

        regular_times.append(formatted_time)

    return regular_times

def check_consecutive_slots(time_dict):
    """
    Checks consecutive time slots in a dictionary and returns a new dictionary describing true or false.
    """
    time_slots = sorted(time_dict.keys())
    time_ranges = generate_time_ranges(time_slots)

    result = {}

    for i in range(len(time_slots) - 1):
        if time_dict[time_slots[i]] == "1" and time_dict[time_slots[i + 1]] == "1":
            result[time_ranges[i]] = "true"
        else:
            result[time_ranges[i]] = "false"

    return result

# Testing dictionary
emptydict = {900: "1", 915: "1", 930: "0"}

# Running the function
result = check_consecutive_slots(emptydict)
print(result)