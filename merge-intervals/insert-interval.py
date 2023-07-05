from interval import *


def insert_interval(existing_intervals, new_interval):
    output = []
    for i, curr in enumerate(existing_intervals):
        if new_interval.end < curr.start:
            output.append(new_interval)
            return output + existing_intervals[i:]
        elif new_interval.start > curr.end:
            output.append(curr)
        else:
            new_interval = Interval(
                min(new_interval.start, curr.start), max(new_interval.end, curr.end)
            )

    output.append(new_interval)
    return output
