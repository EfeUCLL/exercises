class CircularBuffer:
    def __init__(self, max_size):
        self.__buffer = []
        self.__max_size = max_size

    def add(self, other):
        self.__buffer.append(other)
        if len(self.__buffer) > self.__max_size:
            del self.__buffer[0]

    def __len__(self):
        return len(self.__buffer)

    def __getitem__(self, index):
        return self.__buffer[index]
