class Repeat:
    def __init__(self, num):
        self.__num = num

    def __iter__(self):
        return self

    def __next__(self):
        return self.__num
