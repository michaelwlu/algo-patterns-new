from collections import deque


def find_max_sliding_window(nums, w):
    if len(nums) == 0:
        return 0

    if w > len(nums):
        w = len(nums)

    output = []
    q = (
        deque()
    )  # deque will be used to hold the indices of the window values in desc order
    l = 0

    for r in range(len(nums)):  # slide window right through list
        while (
            q and nums[q[-1]] < nums[r]
        ):  # remove any rightmost (lowest) values that are lower than next value
            q.pop()

        q.append(r)  # add new value

        if q[0] < l:  # if window left slides past largest value, remove it
            q.popleft()

        if (r + 1) >= w:  # only when window has reached/exceeded size
            output.append(nums[q[0]])  # add the leftmost (largest) value to output
            l += 1  # slide window left

    return output
