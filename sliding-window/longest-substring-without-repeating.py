# return length of longest substring
def find_longest_substring(string):
    last_char_index = {}
    start = 0
    sub_len = 0

    for end, char in enumerate(string):
        if char in last_char_index:
            start = max(start, last_char_index[char] + 1)

        sub_len = max(sub_len, end - start + 1)

        last_char_index[char] = end

    return sub_len
