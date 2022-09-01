def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    count = 0
    for period in permanence_period:
        if isinstance(period[0], int) and isinstance(period[1], int):
            if (target_time >= period[0] and target_time <= period[1]):
                count += 1
        else:
            return None
    return count
