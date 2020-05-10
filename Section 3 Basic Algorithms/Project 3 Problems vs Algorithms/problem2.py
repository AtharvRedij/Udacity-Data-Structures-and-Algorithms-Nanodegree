def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    left_index = binary_search(arr, target, start, mid - 1)
    right_index = binary_search(arr, target, mid + 1, end)

    return max(left_index, right_index)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search(input_list, number, 0, len(input_list)-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# expected out Pass

# test case 2
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# expected out Pass

# test case 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# expected out Pass

# test case 4 edge case
test_function([[], -1])
# expected out Pass

# test case 5 edge case
test_function([[1], 0])
# expected out Pass
