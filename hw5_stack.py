

class Stack:

    class Node:

        def __init__(self, data, ref=None):
            self.__data = data
            self.__ref = ref


    def __init__(self):
        self.__top = None
        self.__size = 0


    def push(self, data):
        """
        поэлементное заполнение стека,
        где каждый следующий элемент будет ссылаться на предыдущий
        :param data: элемент, который окажется на верхушке стека
        """
        node = Stack.Node(data, None)

        if self.is_empty():
            self.__top = node

        else:
            self.__top, node.ref = node, self.__top

        self.__size += 1


    def peek(self):
        """
        возвращает верхний элемент
        :return: None or элемент на верхушке стека
        """
        return self.__top


    def pop(self):
        """
        возвращает верхний элемент, удаляя его из стека
        :return: ValueError or верхний элемент
        """

        assert not self.is_empty, ValueError("стек пуст, сначала добавьте элемент с помощью push")

        elem = self.__top.data
        self.__top = self.__top.ref
        self.__size -= 1

        return elem


    def is_empty(self):

        return self.__size == 0


    def clear(self):

        self.__top = None
        self.__size = 0


    def count(self, elem):
        """
        ищет количество вхождений элемента в стек
        :return: int or 0
        """
        iter = self.__top
        c = 0

        for i in range(self.__size):
            if iter.data == elem:
                c += 1
                iter = iter.ref

        return c

    def __get_size(self):
        return self.__size


    size = property(__get_size)