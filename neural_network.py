"""
Author: vtarale
"""

# implementing neural networks


import random
import math

# setting variables
inputs_val = 2
hidden_val = 4
output_val  = 1
inputs, ouput, hidden = [], [], []

training_data = [[1, 1], [0, 1], [1, 0], [1, 0]]
answer_data = [0, 1, 1, 0]

hidden_weigths = [[random.uniform(0, 3), random.uniform(0, 3)], [random.uniform(0, 3), random.uniform(0, 3)], [random.uniform(0, 3), random.uniform(0, 3)], [random.uniform(0, 3), random.uniform(0, 3)]]
print(hidden_weigths)
output_weights = [random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3)]
print(output_weights)

bias = 1
learning_rate = 0.5


# some functions
def activation(x):
    return 1/(1+math.exp(-x))

def predict(inputs: list):
    answers = []
    # y = mx+b
    for i in range(hidden_val):
        answers.append(activation((hidden_weigths[i][0] * inputs[0] + hidden_weigths[i][1] * inputs[1]) + bias))
        print(answers[i])
    
    final_prediction = activation((output_weights[0]*answers[0] + output_weights[1]*answers[1] + output_weights[2]*answers[2] + output_weights[3]*answers[3]) + bias)
    print(final_prediction)

    return final_prediction, answers

def update():
    # calculate answer the backpropogate
    pass

prediction, _ = predict([0, 0])