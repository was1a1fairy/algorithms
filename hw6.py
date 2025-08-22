
class PrintDocument:


    def __init__(self, title: str, count_pages: int):
        self.__title = title
        self.__count_pages = count_pages

    def __str__(self):
        return f"{self.__title}, {self.__count_pages}"


class PrintQueue:


    class Node:

        def __init__(self, document: PrintDocument, prev=None):
            self.document = document
            self.prev = prev


    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0


    def enqueue(self, document):

        node = PrintQueue.Node(document)

        if self.__count == 0:
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node
        self.__count += 1


    def dequeue(self):

        if self.__count == 0:
            return None

        node = self.__head
        self.__head = node.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1
        # почему-то я думала, что оно не сработает, забыла почему
        return node.document


    def peek(self):

        if self.is_empty():
            return None

        return self.__head.document


    def is_empty(self):

        return self.__count == 0


    def __get_count(self):
        return self.__count


    count = property(__get_count)


# пример

doc1 = PrintDocument("bebebe", 12).__str__()
queue = PrintQueue()
queue.enqueue(doc1)
queue.enqueue(doc1)
print(queue.dequeue())