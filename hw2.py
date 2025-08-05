

def max_in_range(arr:list, start:int, end:int):

    length = len(arr)

    assert isinstance(arr, list), "array must be list!"
    assert isinstance(start, int), "start must be int("
    assert isinstance(end, int), "end must be int("

    if start < 0:
        start = 0
    if end > length - 1:
        end = length-1

    max = arr[start]
    indexes = []
    for i in range(start+1, end, 1):
        if max < arr[i]:
            max = arr[i]
            indexes.append(i)

    return max, indexes[len(indexes)-1], indexes[len(indexes)-1] + start

def rotate_and_reverse(arr:list, k:int):

    length = len(arr)

    assert isinstance(arr, list), "arr must be list!!"
    assert isinstance(k, int), "k must be int"

    if k > length:
        k -= length

    array = []
    for i in range(k,0,-1):
        array.append(arr[length-i])

    for i in range(0,length,1):
        arr[length-1-i] = arr[length-1-i-k]

    for i in arr[k::]:
        array.append(i)

    for i in range(length//2):
        array[i], array[length-i-1] = array[length-i-1], array[i]

    return array