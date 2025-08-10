def bubble_sort(arr, key=lambda obg: obg, order_by=lambda x,y: x<y):

    assert isinstance(arr, list), TypeError

    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if order_by(key(arr[j]), key(arr[j+1])):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def selection_sort(arr:list, key=lambda obj:obj, order_by=lambda x, y: x > y):

    assert isinstance(arr, list), TypeError

    swap = 0 # счетчик операций смены элементов
    c = 0 # comparison, счетчик операций сравнения
    length = len(arr)

    for i in range(length-1):
        itarget = i

        for j in range(i+1, length):

            c += 1
            if order_by(key(arr[j]),key(arr[itarget])):
                itarget = j

        arr[i], arr[itarget] = arr[itarget], arr[i]
        swap += 1
    return arr, swap, c

def recursive_sum(array:list):

    if len(array) == 1:
        return array[0]

    if len(array) == 0:
        return 0

    return array[len(array)-1] + recursive_sum(array[:len(array)-1:])

def recursive_max(array:list, n: int):

    if n == 0:
        return array[0]

    elem = recursive_max(array, n-1)
    if array[n] < elem:
        return elem

    return array[n]

def recursive_sum_even(array:list, n:int)->int:

    return array[n] + recursive_sum_even(array, n-1) if array[n]%2==0 else 0
