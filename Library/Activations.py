import math

# sigmoid function
def sigmoid(x):
    # bug
    val =  math.exp(1/1+(math.exp(-1*x)))
    print(f"Sigmoid:{val}")
    return val

# derivative of it
def derivative_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))