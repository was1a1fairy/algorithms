def max_in_range(arr:list, start:int, end:int):

    assert isinstance(arr, list), "array must be list!"
    assert isinstance(start, int), "start must be int("
    assert isinstance(end, int), "end must be int("

    if start < 0:
        start = 0
    if end > len(arr) - 1:
        end = len(arr)-1

    max = arr[start]
    indexes = []
    for i in range(start+1, end, 1):
        if max < arr[i]:
            max = arr[i]
            indexes.append(i)

    return max, indexes[len(indexes)-1], indexes[len(indexes)-1] + start