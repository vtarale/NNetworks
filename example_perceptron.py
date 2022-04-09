# a test to check if the preceptron works

import Library.Neural_network as brain
from Library.Vector import Vector

print("Hello World")

perceptron = brain.Perceptron(2, [], 0.1, False)
perceptron.display()

for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
    if i % 2 == 0:
        # let's calculate the error and correct
        error = 1 - perceptron.predict([i, i+5])
        print(error)
        perceptron.correct(error, Vector([i, i+5]))
    else: 
        # let's calculate the error and correct
        error = 0 - perceptron.predict([i, i-5])
        print(error)
        perceptron.correct(error, Vector([i, i-5]))

    perceptron.display()
    prediction = perceptron.predict([2, 5])
    print(prediction)

prediction = perceptron.predict([2, 5])