def add_time(start, duration, day=None):
    day_map = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    timepoint, midday = start.split()
    hour, minute = list(map(int,timepoint.split(":")))
    if midday == "PM":
        hour += 12
    duration_hour, duration_minute = list(map(int,duration.split(':')))
    total_min = minute + duration_minute
    ans_min = total_min % 60
    extra_hour = total_min // 60
    total_hour = hour + duration_hour + extra_hour
    ans_hour = (total_hour % 24) % 12
    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)
    total_day = total_hour // 24
    if total_hour % 24 <= 11:
        ans_midday = "AM"
    else:
        ans_midday = "PM"
    if ans_min <= 9:
        ans_min = '0' + str(ans_min)
    else:
        ans_min = str(ans_min)
    result = ans_hour + ":" + ans_min + " " + ans_midday
    if day == None:
        if total_day == 0:
            return result
        elif total_day == 1:
            return result + ' (next day)'
        return result + ' (' + str(total_day) + ' days later)'
    else:
        ans_day = (day_map.index(day.lower().capitalize()) + total_day) % 7
        if total_day == 0:
            return result + ', ' + day_map[ans_day]
        elif total_day == 1:
            return result + ', ' + day_map[ans_day] + ' (next day)'
        return result + ', ' + day_map[ans_day] + ' (' + str(total_day) + ' days later)'