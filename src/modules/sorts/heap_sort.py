def _heap(parameters: list, n: int, i: int):
    '''
    Maintain the heap sequence
    '''
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and parameters[left] > parameters[largest]:
        largest = left
    if right < n and parameters[right] > parameters[largest]:
        largest = right
    if largest != i:
        parameters[i], parameters[largest] = parameters[largest], parameters[i]
        _heap(parameters, n, largest)


def heap_sort(parameters) -> list:
    '''
    Algorithm build "heap" from given data
    Extract elements from the heap and place max element to the end
    '''
    n = len(parameters)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        _heap(parameters, n, i)

    # Swap max to end
    for i in range(n - 1, 0, -1):
        parameters[i], parameters[0] = parameters[0], parameters[i]
        _heap(parameters, i, 0)

    return parameters
