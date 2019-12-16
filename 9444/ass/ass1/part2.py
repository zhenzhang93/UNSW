#!/usr/bin/env python3
"""
part2.py

UNSW COMP9444 Neural Networks and Deep Learning

ONLY COMPLETE METHODS AND CLASSES MARKED "TODO".

DO NOT MODIFY IMPORTS. DO NOT ADD EXTRA FUNCTIONS.
DO NOT MODIFY EXISTING FUNCTION SIGNATURES.
DO NOT IMPORT ADDITIONAL LIBRARIES.
DOING SO MAY CAUSE YOUR CODE TO FAIL AUTOMATED TESTING.
"""
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt


class LinearModel:
    def __init__(self, num_inputs, learning_rate):
        """
        Model is very similar to the Perceptron shown in Lectures 1c, slide 12, except that:
        (1) the bias is indexed by w(n+1) rather than w(0), and
        (2) the activation function is a (continuous) sigmoid rather than a (discrete) step function.

        x1 ----> * w1 ----\
        x2 ----> * w2 -----\
        x3 ----> * w3 ------\
        ...
                             \
        xn ----> * wn -------+--> s --> activation ---> z
        1  ----> * w(n+1) --/
        """
        self.num_inputs = num_inputs
        self.lr = learning_rate
        self.weights = np.asarray([1.0, -1.0, 0.0])  # Initialize as straight line

    def activation(self, x):
        """
        TODO: Implement a sigmoid activation function that accepts a float and returns
        a float, but raises a Value error if a boolean, list or numpy array is passed in
        hint: consider np.exp()
        """
        if not isinstance(x, float) or not isinstance(x, np.float64):
            raise ValueError
        res = 1 / (1 + np.exp(-x))
        return res

    def forward(self, inputs):
        """
        TODO: Implement the forward pass (inference) of a the model.

        inputs is a numpy array. The bias term is the last element in self.weights.
        hint: call the activation function you have implemented above.
        """
        inputs = np.insert(inputs, 2, 1, axis=0)
        fx = np.dot(self.weights, inputs)
        hx = self.activation(fx)
        return hx

    @staticmethod
    def loss(prediction, label):
        """
        TODO: Return the cross entropy for the given prediction and label
        hint: consider using np.log()
        """
        # −t log(z)−(1−t)log(1−z), z = prediction
        return -(label * np.log(prediction) + (1 - label) * np.log(1 - prediction))

    @staticmethod
    def error(prediction, label):
        """
        TODO: Return the difference between the label and the prediction

        For example, if label= 1 and the prediction was 0.8, return 0.2
                     if label= 0 and the preduction was 0.43 return -0.43
        """
        # t - z
        if label == 1:
            return 1 - prediction
        if label == 0:
            return -prediction

    def backward(self, inputs, diff):
        """
        TODO: Adjust self.weights by gradient descent

        We take advantage of the simplification shown in Lecture 2b, slide 23,
        to compute the gradient directly from the differential or difference
        dE/ds = z - t (which is passed in as diff)

        The resulting weight update should look essentially the same as for the
        Perceptron Learning Rule (shown in Lectures 1c, slide 11) except that
        the error can take on any continuous value between -1 and +1,
        rather than being restricted to the integer values -1, 0 or +1.

        Note: Numpy arrays are passed by reference and can be modified in-place
        """
        inputs = np.insert(inputs, 2, 1, axis=0)
        # w = w - lr *(z - t)*x =  w + lr*(t-z) *x
        # self.weights = self.weights + self.lr * inputs * diff
        self.weights[0] += self.lr * diff * inputs[0]
        self.weights[1] += self.lr * diff * inputs[1]
        self.weights[2] += self.lr * diff * inputs[2]

    def plot(self, inputs, marker):
        """
        Plot the data and the decision boundary
        """
        xmin = inputs[:, 0].min() * 1.1
        xmax = inputs[:, 0].max() * 1.1
        ymin = inputs[:, 1].min() * 1.1
        ymax = inputs[:, 1].max() * 1.1

        x = np.arange(xmin * 1.3, xmax * 1.3, 0.1)
        plt.scatter(inputs[:25, 0], inputs[:25, 1], c="C0", edgecolors='w', s=100)
        plt.scatter(inputs[25:, 0], inputs[25:, 1], c="C1", edgecolors='w', s=100)

        plt.xlim((xmin, xmax))
        plt.ylim((ymin, ymax))
        plt.plot(x, -(self.weights[0] * x + self.weights[2]) / self.weights[1], marker, alpha=0.6)
        plt.title("Data and decision boundary")
        plt.xlabel("x1")
        plt.ylabel("x2").set_rotation(0)


def main():
    inputs, labels = pkl.load(open("../data/binary_classification_data.pkl", "rb"))

    epochs = 400
    model = LinearModel(num_inputs=inputs.shape[1], learning_rate=0.01)

    for i in range(epochs):
        num_correct = 0
        for x, y in zip(inputs, labels):
            # Get prediction
            output = model.forward(x)

            # Calculate loss
            cost = model.loss(output, y)

            # Calculate difference or differential
            diff = model.error(output, y)

            # Update the weights
            model.backward(x, diff)

            # Record accuracy
            preds = output > 0.5  # 0.5 is midline of sigmoid
            num_correct += int(preds == y)

        print(f" Cost: {cost:8.6f} Accuracy: {num_correct / len(inputs) * 100}%")
        model.plot(inputs, "C2--")
    model.plot(inputs, "k")
    plt.show()


if __name__ == "__main__":
    main()
