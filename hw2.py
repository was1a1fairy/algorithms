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

def reverse_even_elements(arr:list[int]) -> list:

    if not isinstance(arr, list):  raise TypeError

    start = 0
    end = 0
    list_even = [elem for elem in arr if elem%2==0]
    length = len(arr)

    for i in range(len(list_even)//2):
        while arr[i+start] % 2 != 0:
            start +=1
        while arr[length-1-i-end] % 2 != 0:
            end += 1
        if i + start == length-1-i-end:
            return arr
        arr[i+start], arr[length-1-i-end] = arr[length-1-i-end], arr[i+start]

    # O(n^2)
    return arr


def add_1_to_integer(arr:list[int]) ->list:

    if not isinstance(arr, list):  raise TypeError

    for i in range(len(arr)-1,-1,-1):
        if arr[i] + 1 == 10:
            arr[i] = 0
        else:
            arr[i] += 1
            return arr
    return [1] + arr
    # O(n)
