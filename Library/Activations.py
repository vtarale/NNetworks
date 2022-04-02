import math

# sigmoid function
def sigmoid(x):
    return math.exp(1/1+(-1*x))

# derivative of it
def derivative_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))