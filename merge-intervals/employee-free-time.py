from interval import Interval
import heapq


## METHOD 1: Combine intervals into one list and sort
def employee_free_time(schedule):
    # error checking
    if not schedule:
        return []

    # combine schedules into one list
    intervals = [interval for person in schedule for interval in person]

    # sort intervals
    intervals.sort(key=lambda x: x.start)

    # loop through intervals
    result = []
    # any potential free time can only begin at the end of the first interval
    last_end = intervals[0].end

    for interval in intervals[1:]:  # check starting from the next interval
        if interval.start > last_end:  # if there's a gap, add the gap
            result.append(Interval(last_end, interval.start))

        # whether gap or not, update to the later end time
        last_end = max(last_end, interval.end)

    return result


## METHOD 2:
def employee_free_time_2(schedule):
    # error checking
    if not schedule:
        return []

    # create heap and first populate with the first interval from each employee's schedule
    heap = []
    for i, employee in enumerate(schedule):
        # heap element is tuple that contains start time, end time, employee idx, and interval idx inside enmployee schedule
        heap.append((employee[0].start, employee[0].end, i, 0))

    # heapify using element's first index, which is start time
    heapq.heapify(heap)

    # loop through intervals
    result = []
    # any potential free time can only begin at the end of the first interval
    last_end = heap[0][1]

    while heap:  # check starting from the next earliest interval
        start, end, employee_idx, interval_idx = heapq.heappop(heap)

        if start > last_end:  # if there's a gap, add the gap
            result.append(Interval(last_end, start))

        # whether gap or not, update to the later end time
        last_end = max(last_end, end)

        next_interval_idx = interval_idx + 1

        # if there are more intervals on that employee's schedule, add it to the heap
        if next_interval_idx < len(schedule[employee_idx]):
            next_interval = schedule[employee_idx][next_interval_idx]

            heapq.heappush(
                heap,
                (
                    next_interval.start,
                    next_interval.end,
                    employee_idx,
                    next_interval_idx,
                ),
            )

    return result
