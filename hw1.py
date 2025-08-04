
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

import tkinter
import customtkinter as ctk


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

        if i == len(matrix)-1 :
            count_visitors += int(matrix[i][3])
            list_count.append(count_visitors)

        elif matrix[i][1] == matrix[i-1][1]:
            count_visitors += int(matrix[i][3])

        else:
            list_count.append(count_visitors)
            count_visitors = int(matrix[i][3])

    for _ in range(len(list_count) - 1):
        for i in range(len(list_count) - 1):
            if list_count[i] < list_count[i+1]:
                buff = list_count[i]
                list_count[i] = list_count[i+1]
                list_count[i+1] = buff

    return list_count

def popular_weekday(matrix):

    list_days = []
    count_visitors = 0
    for i in range(0, 7, 1):
        for j in range(0, len(matrix)-7, 7):
            count_visitors += int(matrix[j + i][3])
        list_days.append([i, count_visitors])
        count_visitors = 0

    for _ in range(len(list_days)-1):
        for i in range(len(list_days)-1):
            if list_days[i][1] < list_days[i + 1][1]:
                list_days[i], list_days[i + 1] = list_days[i + 1], list_days[i]

    for i in range(len(list_days)):
        if list_days[i][0] == 0:
            list_days[i][0] = "Monday"
        elif list_days[i][0] == 1:
            list_days[i][0] = "Tuesday"
        elif list_days[i][0] == 2:
            list_days[i][0] = "Wednesday"
        elif list_days[i][0] == 3:
            list_days[i][0] = "Thursday"
        elif list_days[i][0] == 4:
            list_days[i][0] = "Friday"
        elif list_days[i][0] == 5:
            list_days[i][0] = "Saturday"
        elif list_days[i][0] == 6:
            list_days[i][0] = "Sunday"

    return list_days


root = ctk.CTk()
root.title("task 5")


def command():
    """for button click, show statistics"""
    path = entry1.get()
    label1 = ctk.CTkLabel(root, text="Popular month:")
    label1.pack()
    inf = popular_month(modern_to_matrix(path))[0]
    label2 = ctk.CTkLabel(root, text=inf)
    label2.pack()
    label3 = ctk.CTkLabel(root, text="Popular weekdays:\n(top-3)")
    label3.pack()
    inf = f"1.{popular_weekday(modern_to_matrix(path))[0][0]}, 2.{popular_weekday(modern_to_matrix(path))[1][0]}, 3.{popular_weekday(modern_to_matrix(path))[2][0]}"
    label4 = ctk.CTkLabel(root, text=inf)
    label4.pack()
    label5 = ctk.CTkLabel(root, text="Unpopular days:\n(top-3)")
    label5.pack()
    inf = f"1.{popular_weekday(modern_to_matrix(path))[6][0]}, 2.{popular_weekday(modern_to_matrix(path))[5][0]}, 3.{popular_weekday(modern_to_matrix(path))[4][0]}"
    label6 = ctk.CTkLabel(root, text=inf)
    label6.pack()



entry1 = ctk.CTkEntry(root)
button1 = ctk.CTkButton(root, command=command)

entry1.pack()
button1.pack()


root.mainloop()

print(popular_weekday(modern_to_matrix("file")))