# 3 очередь

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
        """
        добавление элемента в конец очереди
        """

        node = PrintQueue.Node(document)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node
        self.__count += 1


    def dequeue(self):
        """
        удаляет элемент из начала очереди и возвращает его
        """

        if self.is_empty():
            return None

        node = self.__head
        self.__head = node.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1
        # почему-то я думала, что оно не сработает, забыла почему
        return node.document


    def peek(self):

        if not self.is_empty():
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



# 1


class PersonCard:

    def __init__(self, name: str, age: int, occupation:str):
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    def __str__(self):
        return f"{self.__name}, {self.__age}, {self.__occupation}"

class Node:

    def __init__(self, data:PersonCard, next=None):
        self.data = data
        self.next = next


class PersonList:


    def __init__(self):
        self.__count = 0
        self.__head = None


    def is_empty(self):
        return self.__count == 0


    def add_person(self, person:PersonCard):
        """
        добавляет карточку в начало списка
        """
        if self.is_empty():
            node = Node(person, None)
        else:
            node = Node(person, self.__head)
        self.__head = node
        self.__count += 1


    def append_person(self, person: PersonCard):
        """
        добавляет новую карточку в конец списка
        """
        node = Node(person, None)

        if self.is_empty():
            self.__head = node
        else:
            iterator = self.__head
            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = node
        self.__count += 1


    def insert_person_at(self, index:int, person:PersonCard):
        """
        добавляет новую карточку по индексу
        индекс от 0 до self.count -1
        """
        if not isinstance(index, int):  raise TypeError
        if index >= self.__count or index <= 0:  raise ValueError

        iter = self.__head
        for i in range(index-1):
            iter = iter.next

        node = Node(person, iter.next)
        iter.next = node


    def remove_first_person(self):
        """
        удаляет карточку из головы(переназначает self.head)
        """

        if self.is_empty():
            return None

        node = self.__head

        if self.__count == 1:
            return node

        self.__head = self.__head.next
        self.__count -= 1
        return node


    def remove_last_person(self):
        """
        удаляет последнюю добавленную карточку
        """
        iter = self.__head
        while iter.next.next is not None:
            iter = iter.next
        node = iter
        iter = None
        return node


    def remove_person(self, person: PersonCard):
        """
        удаляет карточки, соответствующие переданному значению
        """
        iter = self.__head
        while iter.next is not None:
            if iter.next.person == person:
                iter.next = iter.next.next
                self.__count -= 1
            iter = iter.next

    def clear_all(self):
        self.__count = 0
        self.__head = None


    def total_people(self):
        return self.__count


# 2

class ProjectTask:

    def __init__(self, description:str, duedate:DateTime):
        self.duedate = duedate
        self.description = description

    def __str__(self):
        return f"{self.description}, {self.duedate}"


class TaskStack:

    class Node:

        def __init__(self, data:ProjectTask, ref=None):
            self.data = data
            self.ref = ref


    def __init__(self):
        self.__top = None
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def count(self):
        return self.__count

    def push(self, task: ProjectTask):
        """
        добавляет элемент в стек(на верхушку)
        """
        node = TaskStack.Node(task, self.__top)

        self.__top = node
        self.__count += 1


    def peek(self):
        """
        возвращает вершину стека
        :return: self.__top or none 
        """
        if not self.is_empty():  return self.__top.data

    def pop(self):
        """
        удаляет элемент с вершины стека и возвращает его
        :return: self.__top
        """
        task = self.__top.data
        self.__top = self.__top.ref
        self.__count -= 1
        return task
