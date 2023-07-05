from interval import *


# return a new output array consisting of the merged intervals
# intervals input is sorted by starting time
def merge_intervals(intervals):
    if not intervals:
        return None

    output = [intervals[0]]

    for curr_interval in intervals[1:]:
        last_interval = output[-1]

        if curr_interval.start <= last_interval.end:
            last_interval.end = max(last_interval.end, curr_interval.end)
        else:
            output.append(curr_interval)

    return output
