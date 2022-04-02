from Activations import sigmoid, derivative_sigmoid
from Vector import Vector

class Unit:
    def __init__(self, next: int, weigths, w=None):
        if not w:
            self.weigths = Vector([])
            self.weigths.randomize(0, 3)
            return
        self.weigths = Vector(weigths)
    # display weigths
    def display(self):
        print(self.weigths)

class NNetwork:
    def __init__(self):
        pass