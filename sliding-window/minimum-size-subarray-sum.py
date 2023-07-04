# find the minimum length of a contiguous subarray whose sum is greater than or equal to the target
def min_sub_array_len(target, nums):
    start = 0
    curr_sum = 0
    min_length = float("inf")

    for end, val in enumerate(nums):
        curr_sum += val

        while curr_sum >= target:
            min_length = min(min_length, end - start + 1)

            curr_sum -= nums[start]
            start += 1

    return min_length if min_length != float("inf") else 0
