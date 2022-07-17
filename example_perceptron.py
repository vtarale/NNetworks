# a test to check if the preceptron works

import Library.Neural_network as brain
from Library.Vector import Vector

print("Hello World")

perceptron = brain.Perceptron(2, [], 0.5, False)
perceptron.display()

count = 1

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
    if count % 15 == 0:
        # let's calculate the error and correct
        prediction = perceptron.predict([i, i+5])
        print(f"Prediction: {prediction}")
        error = prediction - 1
        print(f"Error: {error}")
        if error != 0:
            perceptron.correct(error, Vector([i, i+5]))
    else: 
        # let's calculate the error and correct
        prediction = perceptron.predict([i, i-5])
        print(f"Prediction: {prediction}")
        error = prediction - 0.5
        print(f"Error: {error}")
        if error != 0:
            perceptron.correct(error, Vector([i, i-5]))

    perceptron.display()
    count = count + 1

prediction = perceptron.predict([2, 5])
print(f"Final Prediction: {prediction}")