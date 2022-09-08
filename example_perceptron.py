# a test to check if the preceptron works

import Library.Neural_network as brain
from Library.Vector import Vector

print("Hello World")

perceptron = brain.Perceptron(2, [], 1, True)
perceptron.display()

gate = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

epochs = 10

for epoch in range(epochs):
    print(f"Epoch: {epoch}")
    for g in gate:
        nlist = g
        if (nlist[0] == -1 and nlist[1] == -1) or (nlist[0] == 1 and nlist[1] == 1):
            # correct and calculate error
            prediction = perceptron.predict(nlist)
            print(f"Prediction, a: {prediction}")
            error = prediction-1
        else:
            # correct and calculate error
            prediction = perceptron.predict(nlist)
            print(f"Prediction, b: {prediction}")
            error = prediction-0
        error = round(error, 2)
        print()
        if error != 0:
            print(f"Error: {error}")
            perceptron.correct(error, Vector(nlist))
    print()

prediction = perceptron.predict([0, 0])
print(f"Final Prediction: {prediction}")