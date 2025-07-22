# task 1


def max_count_numbers(array: list[int]) -> int:

    if not isinstance(array, list):  raise TypeError

    new_array = []

    for num in array:
        counter = 0
        for number in array:
            if num == number:
                counter += 1
        new_array.append(counter)

    max_count = 0

    for i in range(len(new_array)):
        if new_array[i] > max_count:
            max_count = new_array[i]

    list_max_count_elem = []

    for i in range(len(new_array)):
        if new_array[i] == max_count:
            list_max_count_elem.append(array[i])


    min_elem = list_max_count_elem[0]
  
    for elem in list_max_count_elem:
        if elem < min_elem:
            min_elem = elem
  
    return min_elem
