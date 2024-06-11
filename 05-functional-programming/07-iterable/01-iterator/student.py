class InclusiveRange:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def __iter__(self):
        return InclusiveRangeIterator(self.__num1, self.__num2)


class InclusiveRangeIterator:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start > self.__end:
            raise StopIteration
        next = self.__start
        self.__start += 1
        return next
