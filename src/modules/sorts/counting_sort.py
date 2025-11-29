def counting_sort(parameters: list) -> list:
    '''
    Sorting algorithm that efficient on small range of numbers
    Algorithms count appearances of elements and sort them
    '''
    if not parameters:
        return []

    max_value = max(parameters)
    count = [0] * (max_value + 1)
    output = [0] * len(parameters)

    # counting appearances
    for num in parameters:
        count[num] += 1

    # update values as prefix sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # place numbers on a correct positions
    for num in reversed(parameters):
        output[count[num] - 1] = num
        count[num] -= 1

    return output
