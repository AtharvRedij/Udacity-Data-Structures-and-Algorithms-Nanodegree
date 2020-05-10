def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) != int or number < 0:
        return None

    if number in [0, 1]:
        return number

    start = 0
    end = number//2

    while start <= end:
        middle = (start + end) // 2
        middle_sq = middle ** 2

        if number == middle_sq:
            return middle
        elif number < middle_sq:
            end = middle - 1
        else:
            start = middle + 1
            result = middle

    return result


# Test case 1
print(sqrt(16))
# expected output 4

# Test case 2
print(sqrt(28))
# expected output 5

# Test case 3 edge case
print(sqrt(-2))
# expected output None

# Test case 4 edge case
print(sqrt("100"))
# expected output None
