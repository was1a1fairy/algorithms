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

        if self.__size == self.__count:
            self.__memory = realloc(self.__memory, self.__size)

        for i in range(self.__count, index,-1):
            self.__memory[i] = self.__memory[i-1]

        self.__memory[index] = elem