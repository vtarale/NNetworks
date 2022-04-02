import random

class Vector:
    def __init__(self, vals: list):
        self.vals = vals
    # some math operations
    def add_new(self, vector):
        new = []
        for index in range(len(vector)):
            new.append(self.vals[index] + vector.vals[index])
        return Vector(new)
    def sub_new(self, vector):
        new = []
        for index in range(len(vector)):
            new.append(self.vals[index] - vector.vals[index])
        return Vector(new)
    def multiply_new(self, vector):
        new = []
        for index in range(len(vector)):
            new.append(self.vals[index] * vector.vals[index])
        return Vector(new)
    def div_new(self, vector):
        new = []
        for index in range(len(vector)):
            new.append(self.vals[index] / vector.vals[index])
        return Vector(new)
    # some more
    def add(self, vector):
        for index in range(len(vector)):
            self.vals[index] = self.vals[index] + vector.vals[index]
    def sub(self, vector):
        for index in range(len(vector)):
            self.vals[index] = self.vals[index] + vector.vals[index]
    def multiply(self, vector):
        for index in range(len(vector)):
            self.vals[index] = self.vals[index] * vector.vals[index]
    def div(self, vector):
        for index in range(len(vector)):
            self.vals[index] = self.vals[index] / vector.vals[index]
    # dot product
    def dot(self, vector):
        dot = 0
        for index in range(len(vector)):
            dot += self.vals[index] * vector.vals[index]
        return dot
    # extras
    def randomize(self, x: float, y: float):
        for index in range(len(self.vals)):
            self.vals[index] = random.uniform(x, y)