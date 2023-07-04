def min_window(str1, str2):
    p1, p2 = 0, 0
    min_sub = ""

    while p1 < len(str1):
        if str1[p1] == str2[p2]:
            p2 += 1

            if p2 == len(str2):
                end = p1

                p2 -= 1  # only decrement p2 back into range since p1 hasn't incremented yet

                while p2 >= 0:
                    if str1[p1] == str2[p2]:
                        p2 -= 1

                    p1 -= 1

                p1 += 1

                if min_sub == "" or end - p1 + 1 < len(min_sub):
                    min_sub = str1[p1 : end + 1]  # remember to include end aka p1

                p2 = 0

        p1 += 1

    return min_sub
