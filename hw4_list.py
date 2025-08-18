def realloc(memory, old_size):
    """
    увеличение массива с элементами добавлением элементов None,
    которых в два раза меньше чем было элементов до.

    :param memory: list[elem](self.__memory)
    :param old_size: int(self.__count)
    :return: list[elem,elem,None]
    """
    new_memory = malloc(old_size + old_size//2)

    for i in range(old_size):
        new_memory[i] = memory[i]

    return new_memory


def malloc(count):
    """
    выделение памяти для массива

    :param count: int
    :return: list([None,None,None...]
    """
    return [None] * count


class List:


    def __init__(self):
        self.__count = 0
        self.__size = 4
        self.__memory = [None,None,None,None]


    def add(self, elem):
        """
        append(добавление элемента в конец массива)
        """

        if self.__size == self.__count:
            self.__memory = realloc(self.__memory, self.__size)

        self.__memory[self.__count] = elem
        self.__count += 1


    def remove(self, elem):
        """
        удаление элемента из массива
        (все непустые элементы после него сдвигаются на 1 влево,
        чтобы не было пустого элемента посередине)
        """

        itarget = -1

        for i in range(0, self.__count, 1):
            if self.__memory[i] == elem:
                itarget = i

        if itarget == -1:  return

        for i in range(itarget, self.__count-1, 1):
            self.__memory[i] = self.__memory[i+1]

        self.__count -= 1
        self.__memory[self.__count] = None


    def insert(self, index, elem):
        """
        вставляет элемент по индексу
        (все элементы после соответственно сдвигаются вправо)
        """

        assert index < self.__count or index > 0, ValueError

        if self.__size == self.__count:
            self.__memory = realloc(self.__memory, self.__size)

        for i in range(self.__count, index,-1):
            self.__memory[i] = self.__memory[i-1]

        self.__memory[index] = elem

    def pop(self, index):
        """
        удаляет элемент по индексу,
        сдвигает последующие элементы,
        чтобы не образовывался пустой элемент
        """

        assert index < self.__count or index > 0, ValueError

        for i in range(index, self.__count-1, 1):
            self.__memory[i] = self.__memory[i+1]

        self.__count -= 1
        self.__memory[self.__count] = None


    def is_empty(self):
        """
        если массив пустой -> true, иначе -> false
        :return: bool
        """
        return self.__count == 0


    def clear(self):
        """
        очищает массив(путем выделения новой памяти стандартного размера,
        заданного в конструкторе)
        """
        self.__memory = malloc(4)

    def find(self, elem):
        """
        ищет индекс заданного элемента
        :return: int(index or -1 if not elem in list)
        """

        for i in range(self.__count):
            if self.__memory[i] == elem:
                return i

        return -1

    def count_elem(self, elem):
        """
        ищет количество элементов в массиве
        :param elem: искомый элемент
        :return: int(count elems)
        """

        c = 0
        for i in range(self.__count):
            if self.__memory[i] == elem:
                c += 1

        return c

    def __get_count(self):

        return self.__count

    def __get_memory(self):

        return self.__memory

    count = property(__get_count)
    memory = property(__get_memory)