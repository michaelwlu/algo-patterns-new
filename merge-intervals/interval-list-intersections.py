from interval import Interval


# Function to find the intersecting points between two intervals
def intervals_intersection(interval_list_a, interval_list_b):
    result = []
    a = b = 0

    # end once we've reached the end of either list
    while a < len(interval_list_a) and b < len(interval_list_b):
        i_a, i_b = interval_list_a[a], interval_list_b[b]

        start = max(i_a.start, i_b.start)  # get the later start time
        end = min(i_a.end, i_b.end)  # get the earlier end time

        if start <= end:  # if the times overlap, the intervals overlap
            result.append(Interval(start, end))  # add the intersection

        # we can now move on from the earlier ending interval
        if i_a.end < i_b.end:
            a += 1
        else:
            b += 1

    return result
