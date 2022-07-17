import math

# sigmoid function
def sigmoid(x):
    # bug
    func = lambda x: .5 * (math.tanh(.5 * x) + 1)
    val = func(x)
    val = round(val, 2)
    return val

# derivative of it
def derivative_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))