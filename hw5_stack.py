

class Stack:

    class Node:

        def __init__(self, data, ref=None):
            self.__data = data
            self.__ref = ref


    def __init__(self):
        self.__top = None
        self.__count = 0


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
            self.__top = node
            node.ref = self.__top

        self.__count += 1


    def peek(self):
        """
        возвращает верхний элемент
        :return: None or элемент на верхушке стека
        """
        if self.is_empty():
            return None

        return self.__top.data


    def pop(self):
        """
        возвращает верхний элемент, удаляя его из стека
        :return: ValueError or верхний элемент
        """
        if self.is_empty():
            return None

        elem = self.__top.data
        self.__top = self.__top.ref
        self.__count-= 1

        return elem


    def is_empty(self):

        return self.__count == 0


    def clear(self):

        self.__top = None
        self.__count = 0


    def __get_count(self):
        return self.__count


    size = property(__get_count)