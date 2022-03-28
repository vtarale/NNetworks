import math

def sigmoid(x):
    return math.exp(1/1+(-1*x))

def derivative_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))