def find_repeated_sequences(s, k):
    window_size = k
    seq_len = len(s)

    output = set()
    if seq_len < window_size:
        return output

    seen = set()
    base = 4

    mapping = {"A": 1, "G": 2, "C": 3, "T": 4}
    nums = []
    for i in range(seq_len):
        nums.append(mapping.get(s[i]))

    hash_value = 0

    for start in range(seq_len - window_size + 1):
        if start == 0:
            for end in range(window_size):
                hash_value = hash_value * base + nums[end]
        else:
            hash_value = (
                hash_value - (nums[start - 1] * pow(base, window_size - 1))
            ) * base + nums[start + window_size - 1]

        if hash_value in seen:
            output.add(s[start : start + window_size])
        else:
            seen.add(hash_value)

    return output
