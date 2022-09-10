# implementing neural networks
import random

# a perceptron
class Unit:
    def __init__(self, learning_rate: float, inputs: int):
        self.learning_rate =learning_rate
        self.weigths = []
        print(inputs)

        for _ in range(inputs):
            self.weigths.append(random.uniform(0, 3))

        print(self.weigths)

dummy_unit = Unit(1, 5)