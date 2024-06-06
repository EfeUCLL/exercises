class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, item):
        self.__queue.append(item)

    def next(self):
        firstQueue = self.__queue[0]
        self.__queue.remove(firstQueue)
        return firstQueue

    def is_empty(self):
        return len(self.__queue) == 0
