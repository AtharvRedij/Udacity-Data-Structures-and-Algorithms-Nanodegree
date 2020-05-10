def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_zero_index = 0
    next_two_index = len(input_list) - 1

    front = 0

    while front <= next_two_index:
        if input_list[front] == 0:
            input_list[front] = input_list[next_zero_index]
            input_list[next_zero_index] = 0
            next_zero_index += 1
            front += 1
        elif input_list[front] == 2:
            input_list[front] = input_list[next_two_index]
            input_list[next_two_index] = 2
            next_two_index -= 1
        else:
            front += 1

    return input_list


def test_function(test_case):
    if test_case in ["", None]:
        print("Invalid Input")
        return

    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# test case 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# expected output Pass

# test case 2
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# expected output Pass

# test case 3 edge case
test_function([])
# expected output Pass

# test case 4 edge case
test_function(None)
# expected output Invalid Input
