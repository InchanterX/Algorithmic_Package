def quick_sort(parameters: list) -> list:
    '''
    Really quick sort. It is even cold quick sort.
    Split array into two parts. Smaller to left, greater to right and make a recursive call of new parts.
    '''
    # base case
    if len(parameters) < 2:
        return parameters
    # sorting
    else:
        pivot = parameters[0]
        less = [i for i in parameters[1:] if i < pivot]
        greater = [i for i in parameters[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
