class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width

    @property
    def volume(self):
        return self.width * self.height * self.depth