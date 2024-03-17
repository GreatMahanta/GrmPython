# Explanation: The function should return an empty list when the
# third argument (step) plus third argument is greater than the second argument
# and return a list of integers from start to end plus step

# summary:
# creatind range(a, b, c) without using function range(a, b, c)!


def new_range(start, end, step=1):

    final_list = []
    counter = start

    if start + step < end:
        while counter < end:
            final_list.append(start)
            start += step
            counter += step
    else:
        return final_list

    return final_list


print(new_range(7, 20, 3))  # general test -> [7, 10, 13, 16, 19]
print(new_range(4, 9, 7))  # special test -> []

# and better implement is:


def better_new_range(start, end, step=1):

    final_list = []

    if start + step < end:
        while start < end:
            final_list.append(start)
            start += step
    else:
        return final_list

    return final_list


print(better_new_range(7, 20, 3))  # general test -> [7, 10, 13, 16, 19]
print(better_new_range(4, 9, 7))  # special test -> []
