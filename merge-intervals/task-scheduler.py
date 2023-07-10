import heapq
from collections import deque, Counter


# Method 1: use max heap and queue
def least_time(tasks, n):
    # count frequency of each task
    freq = Counter(tasks)

    # create max heap of frequency values (convert to negative for use in python's min heap)
    heap = [-count for count in freq.values()]
    heapq.heapify(heap)

    queue = deque()  # pairs of (-count, next_time)
    time = 0

    while heap or queue:
        time += 1

        if heap:
            count = heapq.heappop(heap)
            count += 1

            if count < 0:
                queue.append((count, time + n))

        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.popleft()[0])

    return time


# Method 2: use queue only
def least_time(tasks, n):
    if n == 0:
        return len(tasks)

    # Sort the array in order of max frequency
    count = Counter(tasks)
    frequencies = list(count.values())
    frequencies.sort(reverse=True)

    # For each frequency, associate it with the time at which it can be ran. Use +1 to offset 0-indexing
    jobs = deque([i + 1, j] for i, j in enumerate(frequencies))

    # Start the time variable at 0, so once we enter the loop we will be at time '1'
    # This allows us to directly return time at the end.
    time = 0

    while jobs:
        time += 1
        if time < jobs[0][0]:
            continue

        cur_turn, cur_freq = jobs.popleft()
        cur_freq -= 1
        if cur_freq > 0:
            jobs.append([cur_turn + n + 1, cur_freq])

    return time


# Method 3: calculate time based on number of max repeats
def least_time(tasks, n):
    # count most repeated task
    freq = Counter(tasks)
    max_task_freq = max(freq.values())

    # find how many other tasks repeat this often
    other_tasks = Counter(freq.values())[max_task_freq] - 1

    return max(len(tasks), max_task_freq * (n + 1) - n + other_tasks)
