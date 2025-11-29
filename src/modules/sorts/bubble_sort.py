def bubble_sort(parameters: list) -> list:
    '''
    Bubble sort algorithm that sort array by raising up greater elements up inside the array while it won't be sorted
    '''
    n = len(parameters)
    print(parameters)
    while n > 0:
        last = 0
        for i in range(1, n):
            if parameters[i-1] > parameters[i]:
                parameters[i-1], parameters[i] = parameters[i], parameters[i-1]
                last = i
        n = last
    return parameters
