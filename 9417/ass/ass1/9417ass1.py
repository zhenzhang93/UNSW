import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

J_theta = []

def minmax(x, min_x, max_x):
    return (x - min_x) / (max_x - min_x)


def RMSE(X, y, theta0, theta1):
    res = 0
    for i in range(len(X)):
        res += (y[i] - (theta0 + X[i] * theta1)) ** 2
    res = res / len(X)
    return pow(res, 0.5)


def gradient_descent(a, max_iter, theta0, theta1, X, y):
    cur_iter = 0
    newy = y.values.reshape(len(y), 1)
    error0 = sum((newy - (theta0 + X * theta1)) ** 2)
    # plt.ion()
    while cur_iter < max_iter:
        # stochastic gradient descent

        for i in range(len(X)):
            diff = y[i] - (theta0 + X[i] * theta1)
            theta0 += a * diff * 1
            theta1 += a * diff * X[i]

        # batch gradient descent

        J_theta.append(RMSE(X, y, theta0, theta1))

        """
        res0, res1 = 0, 0
        for i in range(len(X)):
            diff = y[i] - (theta0 + X[i] * theta1)
            res0 += diff * 1
            res1 += diff * X[i]

        theta0 += a * res0 / len(X)
        theta1 += a * res1 / len(X)
        """

        # print(theta0, theta1)
        cur_iter += 1
        # plt.scatter(X, y, color='blue')
        # plt.plot(X, theta0 + X * theta1, color='red')
        # print(RMSE(X, y, theta0, theta1))
        # print(cur_iter)
        # plt.show()
        # plt.pause(0.01)
        # plt.clf()
        error1 = sum((newy - (theta0 + X * theta1)) ** 2)
        if abs(error1 - error0) < 0.000001:
            break
        error0 = error1

    return theta0, theta1


data = pd.read_csv('Advertising.csv')
features = ['TV']
# scaler = MinMaxScaler()
X = data[features][:-10]
y = data.Sales[:-10]

max_x = max(X.TV)
min_x = min(X.TV)

X_test = data[features][-10:]
y_test = data.Sales[-10:]

# scaler.fit(X)
Normalisation_data_X = minmax(X, min_x, max_x).values.reshape(len(X),1)
# print(Normalisation_data_X)
xinx = minmax(X_test, min_x, max_x)

theta0, theta1 = gradient_descent(0.01, 500, -1, -0.5, Normalisation_data_X, y)
print(theta0,theta1)
newy_test = y_test.values.reshape(10, 1)
newx_test = xinx.TV.values.reshape(10, 1)

print(RMSE(newx_test, newy_test, theta0, theta1))

#model = LinearRegression()
#model.fit(Normalisation_data_X, y)

#y_predict = model.predict(scaler.transform(X_test))

# print(y_test)
# print(y_predict)

# plt.scatter(X_test, y_test, color='red')
# plt.plot(X_test, y_predict, color='red')
# plt.scatter(X, y, color='blue')
# plt.show()
plt.plot(J_theta, color='red')
# plt.ioff()
plt.show()
