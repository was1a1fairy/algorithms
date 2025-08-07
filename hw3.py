def bubble_sort(arr, key=lambda obg: obg, order_by=lambda x,y: x>y):

    assert isinstance(arr, list), TypeError

    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if order_by(key(arr[j]), key(arr[j+1])):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr