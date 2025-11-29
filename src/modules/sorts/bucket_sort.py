def _insertion_sort(bucket: list) -> list:
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j+1] = bucket[j]
            j -= 1
        bucket[j+1] = key
    return bucket


def bucket_sort(parameters: list) -> list:
    '''
    Bucket sort split given elements to the buckets with index that is closest to the element ratio to buckets amount.
    Then sort buckets using insertion_sort and unite it to the result.
    '''
    n = len(parameters)
    buckets: list[list[int]] = [[] for _ in range(n)]

    # Spreading element to the buckets
    for number in parameters:
        index = int(n * number)
        buckets[index].append(number)

    # Sorting elements in every bucket using insertion sort
    for bucket in buckets:
        bucket = _insertion_sort(bucket)

    # Gather numbers from every bucket together
    index = 0
    for bucket in buckets:
        for number in bucket:
            parameters[index] = number
            index += 1

    return parameters
