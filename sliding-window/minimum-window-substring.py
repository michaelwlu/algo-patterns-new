def min_window(s, t):
    if t == "":
        return ""

    start, end = 0, 0  # sliding window
    count_t, window = (
        {},
        {},
    )  # one hash map to count characters in t, other to count in window
    min_sub = ""

    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
        window[c] = 0  # window does not need keys other than those chars in t

    have, need = 0, len(count_t)  # count for each satisfied character count

    while end < len(s):
        right_char = s[end]

        if right_char in count_t:
            window[right_char] += 1

            if window[right_char] == count_t[right_char]:
                have += 1  # only increment when exact match

        while have == need:
            # all characters found
            # update minimum substring
            if min_sub == "" or end - start + 1 < len(min_sub):
                min_sub = s[start : end + 1]

            # start shrinking window from left by eliminating all non-needed chars
            left_char = s[start]

            if left_char in window:
                if window[left_char] == count_t[left_char]:
                    have -= 1
                window[left_char] -= 1

            start += 1

        end += 1

    return min_sub
