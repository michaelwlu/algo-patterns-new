from interval import Interval
import heapq


# METHOD 1: use a heap to get earliest ending time
def find_sets(intervals):
    # error check
    if not intervals:
        return None

    intervals.sort(key=lambda x: x.start)

    heap = [intervals[0].end]

    for interval in intervals[1:]:
        if interval.start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, interval.end)

    return len(heap)


# METHOD 2: sort start and end times in two lists
def find_sets_2(intervals):
    # error check
    if not intervals:
        return None

	start = sorted([i.start for i in intervals])
    end = sorted([i.end for i intervals])

	res = count = 0
	s = e = 0

	while s < len(intervals):
		if (start[s] < end[e]):
			s += 1
			count += 1

			res = max(res, count)
		else:
			e += 1
			count -= 1

	return res


    