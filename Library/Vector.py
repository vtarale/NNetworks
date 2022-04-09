import random

class Vector:
    def __init__(self, vals: list):
        self.vals = vals
    # some math operations
    def add_new(self, vector):
        new = []
        for index in range(len(vector.vals)):
            new.append(self.vals[index] + vector.vals[index])
        return Vector(new)
    def sub_new(self, vector):
        new = []
        for index in range(len(vector.vals)):
            new.append(self.vals[index] - vector.vals[index])
        return Vector(new)
    def multiply_new(self, vector):
        new = []
        for index in range(len(vector.vals)):
            new.append(self.vals[index] * vector.vals[index])
        return Vector(new)
    def div_new(self, vector):
        new = []
        for index in range(len(vector.vals)):
            new.append(self.vals[index] / vector.vals[index])
        return Vector(new)
    # some more
    def add(self, vector):
        for index in range(len(vector.vals)):
            self.vals[index] = self.vals[index] + vector.vals[index]
    def sub(self, vector):
        for index in range(len(vector.vals)):
            self.vals[index] = self.vals[index] + vector.vals[index]
    def multiply(self, vector):
        for index in range(len(vector.vals)):
            self.vals[index] = self.vals[index] * vector.vals[index]
    def div(self, vector):
        for index in range(len(vector.vals)):
            self.vals[index] = self.vals[index] / vector.vals[index]
    # lot more
    def add_once(self, vector):
        for index in range(len(self.vals)):
            self.vals[index] = self.vals[index] + vector
    def sub_once(self, vector):
        for index in range(len(self.vals)):
            self.vals[index] = self.vals[index] + vector
    def multiply_once(self, vector):
        for index in range(len(self.vals)):
            self.vals[index] = self.vals[index] * vector
    def div_once(self, vector):
        for index in range(len(self.vals)):
            self.vals[index] = self.vals[index] / vector
    # dot product
    def dot(self, vector):
        dot = 0
        for index in range(len(vector.vals)):
            dot += self.vals[index] * vector.vals[index]
        return dot
    # extras
    def randomize(self, x: float, y: float):
        for index in range(len(self.vals)):
            self.vals[index] = random.uniform(x, y)
    def randomize_new(self, x: float, y: float, num: int):
        for _ in range(num):
            self.vals.append(random.uniform(x, y))
    def copy(self):
        return Vector(self.vals)