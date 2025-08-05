import time


def max_in_range(arr:list, start:int, end:int):

    length = len(arr)

    if not isinstance(arr, list):  raise TypeError
    if not isinstance(start, int):  raise TypeError
    if not isinstance(end, int):  raise TypeError

    if start < 0 or start > (length-1):
        start = 0
    if end > length - 1 or end < 0:
        end = length-1

    run = time.time()

    max = arr[start]
    indexes = [0]
    for i in range(start+1, end+1, 1):
        if max < arr[i]:
            max = arr[i]
            indexes.append(i-start)

    print(time.time()-run)
    # O(n^2)
    return max, indexes[len(indexes)-1], indexes[len(indexes)-1]+start


def rotate_and_reverse(arr:list, k:int):

    length = len(arr)

    if not isinstance(arr, list):  raise TypeError
    if not isinstance(k, int):  raise TypeError

    if k > length:
        k %= length

    run = time.time()

    array = []
    for i in range(k,0,-1):
        array.append(arr[length-i])

    for i in range(0,length,1):
        arr[length-1-i] = arr[length-1-i-k]

    for i in arr[k::]:
        array.append(i)

    for i in range(length//2):
        array[i], array[length-i-1] = array[length-i-1], array[i]

    print(time.time() - run)
    # O(n)
    return array