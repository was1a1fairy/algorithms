def realloc(memory, old_size):
    new_memory = malloc(old_size + old_size//2)

    for i in range(old_size):
        new_memory[i] = memory[i]

    return new_memory


def malloc(count):
    return [None] * count


class List:


    def __init__(self):
        self.__count = 0
        self.__size = 4
        self.__memory = [None,None,None,None]


    def add(self, elem):

        if self.__size == self.__count:
            self.__memory = realloc(self.__memory, self.__size)

        self.__memory[self.__count] = elem
        self.__count += 1


    def remove(self, elem):

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

        assert index < self.__count or index > 0, ValueError

        if self.__size == self.__count:
            self.__memory = realloc(self.__memory, self.__size)

        for i in range(self.__count, index,-1):
            self.__memory[i] = self.__memory[i-1]

        self.__memory[index] = elem

    def pop(self, index):

        assert index < self.__count or index > 0, ValueError

        for i in range(index, self.__count-1, 1):
            self.__memory[i] = self.__memory[i+1]

        self.__count -= 1
        self.__memory[self.__count] = None


    def is_empty(self):
        return self.__count == 0


    def clear(self):
        self.__memory = malloc(4)

    def find(self, elem):

        for i in range(self.__count):
            if self.__memory[i] == elem:
                return i

        return -1

    def count(self, elem):

        c = 0
        for i in range(self.__count):
            if self.__memory[i] == elem:
                c += 1

        return c