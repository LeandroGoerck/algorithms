def study_schedule(permanence_period, target_time):
    if type(target_time) is not int or target_time < 0:
        return None
    count = 0
    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None
        if (target_time >= period[0]  and target_time <= period[1]):
            count += 1
    return count
