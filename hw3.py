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

    if n<=0:
        return array[n]
        
    return array[n] + recursive_sum_even(array, n-1) if array[n]%2==0 else 0


def recursive_reverse_string(string:str):

    if len(string)<=1:
        return string

    return string[len(string) - 1] + recursive_reverse_string(string[:len(string) - 1])
    
def recursive_is_palindrome(string:str, i, length):
# i = len(string)//2

    if i<=0:
        return True
    if string[i-1]!=string[length-i]:
        return False

    return recursive_is_palindrome(string, i-1, length)

def recursive_fibonacci(n:int):

    if n<=0:
        return 0
    if n<=2:
        return 1

    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def recursive_sum_of_digits(integer):

    if integer == 0:
        return 0
    
    return integer%10 + recursive_sum_of_digits(integer//10)
