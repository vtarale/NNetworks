from Library.Activations import sigmoid, derivative_sigmoid
from Library.Vector import Vector
import random

class Perceptron:
    def __init__(self, num: int, weigths: list, learning_rate: float, w: bool):
        if w:
            self.weigths = Vector([])
            self.weigths.randomize_new(0, 3, num)
        else:
            self.weigths = Vector(weigths)
        self.bias = random.uniform(0, 3)
        self.learning_rate = learning_rate
    # display weigths
    def display(self):
        print(f"Weigths{self.weigths.vals}")
    # predict
    def predict(self, inputs: list):
        vector_in = Vector(inputs)
        dot = self.weigths.dot(vector_in)
        return sigmoid(dot + self.bias)
    # correct
    def correct(self, error: float, inputs: Vector):
        gradient = inputs.copy()
        gradient.multiply_once(error)
        gradient.multiply_once(self.learning_rate)
        self.weigths.add(gradient)

class NNetwork:
    def __init__(self, inputs: int, hidden: int, outputs: int):
        pass