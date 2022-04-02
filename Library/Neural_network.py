from Activations import sigmoid, derivative_sigmoid
from Vector import Vector
import random

class Unit:
    def __init__(self, next: int, weigths, learning_rate, w=None):
        if not w:
            self.weigths = Vector([])
            self.weigths.randomize(0, 3)
            return
        self.weigths = Vector(weigths)
        self.bias = random.uniform(0, 3)
        self.learning_rate = learning_rate
    # display weigths
    def display(self):
        print(self.weigths)
    # predict
    def predict(self, inputs: list):
        vector_in = Vector(inputs)
        dot = self.weigths.dot(vector_in)
        return sigmoid(dot + self.bias)
    # correct
    def correct(self, error, inputs):
        gradient = Vector(error.vals)
        gradient.multiply(error)
        gradient.multiply(inputs)
        gradient.multiply_once(self.learning_rate)
        self.weigths.add(gradient)

class NNetwork:
    def __init__(self):
        pass