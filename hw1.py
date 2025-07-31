
def check_input(n):
    """
    проверка входных данных
    для всех функций
    """
    if not isinstance(n, int): raise  TypeError


def factorial(n: int) -> int:

    check_input(n)

    result = 1
    while n:
        result *= n
        n -= 1

    return result


def fibonacci(n: int) -> list:
    # [0,1,1,2,3,5]
    check_input(n)

    if n == 0:
        return [0]

    elif n == 1:
        return [0, 1, 1]

    res = [0, 1]
    for i in range(1,n+2):
        if (res[i] + res[i-1]) > n:
            return res
        res.append(res[i-1] + res[i])


def count_ones(n: int) -> int:

    check_input(n)

    count = 0
    while n:
        if n%2 == 1:
            count += 1
        n //= 2

    return count


def is_palindrome(x: int) -> bool:

        check_input(x)

        buff = x
        res = x%10
        while x>10:
            x //= 10
            res = (res*10) + x%10

        return res == buff

# _______________________________________
# _______________________________________

def modern_to_matrix(file):
    file = open(file, "r")
    matrix = [i.split(",") for i in file.readlines()]

    new_matrix = []
    for note in matrix:
        for i in range(len(note)):
            if i == 0:
                new_note1 = note[i].split("-")
            else:
                new_note1.append(note[i].replace("\n", ""))
        new_matrix.append(new_note1)

    return new_matrix

def popular_month(matrix):

    list_count = []
    count_visitors = int(matrix[0][3])
    for i in range(1, len(matrix)):
        if matrix[i][1] == matrix[i-1][1]:
            count_visitors += int(matrix[i][3])
        else:
            list_count.append(count_visitors)
            count_visitors = int(matrix[i][3])

    return max(list_count)

# дни недели потом сделаю