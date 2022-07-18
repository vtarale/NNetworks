# a test to check if the preceptron works

import Library.Neural_network as brain
from Library.Vector import Vector

print("Hello World")

perceptron = brain.Perceptron(2, [], 1, False)
perceptron.display()

gate = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

epochs = 500

for epoch in range(epochs):
    print(f"Epoch: {epoch}")
    for g in gate:
        if g[0] == -1 and g[1] == -1:
            # correct and calculate error
            prediction = perceptron.predict(g)
            print(f"Prediction: {prediction}")
            error = prediction-1
        else:
            # correct and calculate error
            prediction = perceptron.predict(g)
            print(f"Prediction: {prediction}")
            error = prediction-0
        error = round(error, 2)
        print()
        if error != 0:
            print(f"Error: {error}")
            perceptron.correct(error, Vector(g))
    print()

prediction = perceptron.predict([0, 0])
print(f"Final Prediction: {prediction}")