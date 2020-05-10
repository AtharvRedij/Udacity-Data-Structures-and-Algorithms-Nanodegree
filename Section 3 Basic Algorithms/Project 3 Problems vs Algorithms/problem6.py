import random


def get_min_max(arr):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(arr) == 0:
        return None

    min = arr[0]
    max = arr[0]

    for n in arr[1:]:
        if n < min:
            min = n
        if n > max:
            max = n

    return min, max


# Case 1
l = [i for i in range(0, 10)]
random.shuffle(l)
print(get_min_max(l))
# expected output (0, 9)


# Case 2
l = [i for i in range(-100, 19)]
random.shuffle(l)
print(get_min_max(l))
# expected output (-100, 18)


# Case 3 edge case
l = [i for i in range(0, 1)]
random.shuffle(l)
print(get_min_max(l))
# expected output (0, 0)

# Case 4 edge case
l = []
random.shuffle(l)
print(get_min_max(l))
# expected output None
