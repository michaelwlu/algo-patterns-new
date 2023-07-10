def longest_repeating_character_replacement(s, k):
    if k == 0:
        return 0

    # use hash map to track window character frequency
    freq = {}
    start = 0
    longest = 0
    # track max seen repeating characters
    max_repeat = 0

    # slide window end
    for end in range(len(s)):
        end_char = s[end]
        freq[end_char] = freq.get(end_char, 0) + 1

        # longest result will only change if we find a higher max of repeating characters
        max_repeat = max(max_repeat, freq[end_char])

        # slide window start
        while end - start + 1 - max_repeat > k:
            start_char = s[start]
            freq[start_char] -= 1
            start += 1

        # if longer valid window, store new max
        longest = max(longest, end - start + 1)

    return longest
