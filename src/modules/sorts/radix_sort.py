def radix_sort(parameters) -> list:
    '''
    Version of the radix algorithms that works on buckets. It stores digits in 10 buckets for every digit.
    '''
    if not parameters:
        return []

    max_number = max(parameters)
    place = 1  # current place (units, tens, ...)

    # distribute numbers to ten buckets
    while max_number // place > 0:
        buckets: list[list[int]] = [[] for _ in range(10)]

        for number in parameters:
            index = (number // place) % 10
            buckets[index].append(number)

        # gather everything back
        parameters = []
        for bucket in buckets:
            parameters.extend(bucket)

        place *= 10

    return parameters
