import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# from sklearn.model_selection import GridSearchCV


def minmax(x, min_x, max_x):
    return (x - min_x) / (max_x - min_x)


data = pd.read_csv('CreditCards.csv')
X_data = data.drop(['Y'], axis=1)

X_min = np.min(X_data, axis=0)
X_max = np.max(X_data, axis=0)

X_data = minmax(X_data, X_min, X_max)

X_train = X_data[:621]
X_test = X_data[621:]

y_train = data.Y[:621]
y_test = data.Y[621:]
knn_2 = KNeighborsClassifier(n_neighbors=2)
knn_2.fit(X_train, y_train)
y_predict = knn_2.predict(X_test)

print("when k = 2, the accuracy score for test data is", knn_2.score(X_test, y_test))
print("when k = 2, the accuracy score for training data is", knn_2.score(X_train, y_train))
print("when k = 2, the precision score is: ", precision_score(y_test, y_predict))
print("when k = 2, the recall score is: ", recall_score(y_test, y_predict))

a = precision_score(y_test, y_predict)
b = recall_score(y_test, y_predict)

print("when k = 2, the f1-score is: ", 2 * a * b / (a + b))

training_auc_score = []
test_auc_score = []

n_neighbors = range(1, 31)
best_neighbor_number, best_score = None, None

# GridSearchCV
"""
param_grid = {'n_neighbors': n_neighbors}
knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, scoring='roc_auc', cv=10)
knn_cv.fit(X_data, data.Y)
print(knn_cv.best_score_)
print(knn_cv.best_params_)
"""

for neighbors in n_neighbors:
    knn = KNeighborsClassifier(neighbors)
    knn.fit(X_train, y_train)
    y_train_predict_proba = knn.predict_proba(X_train)[:, 1]
    y_predict_proba = knn.predict_proba(X_test)[:, 1]
    training_auc_score.append(roc_auc_score(y_train, y_train_predict_proba))
    test_auc_score.append(roc_auc_score(y_test, y_predict_proba))
    current_score = roc_auc_score(y_test, y_predict_proba)
    if not best_score or best_score < current_score:
        best_score = current_score
        best_neighbor_number = neighbors

print("optimal value for number of k is", best_neighbor_number)

plt.plot(n_neighbors, training_auc_score)
plt.title('Training AUC score')
plt.ylabel('AUC score')
plt.xlabel('n_neighbors')
plt.show()

plt.plot(n_neighbors, test_auc_score)
plt.title('Test AUC score')
plt.ylabel('AUC score')
plt.xlabel('n_neighbors')
plt.show()

knn_5 = KNeighborsClassifier(n_neighbors=5)
knn_5.fit(X_train, y_train)
y_predict = knn_5.predict(X_test)

print("when k = 5, the accuracy score for test data is:", knn_5.score(X_test, y_test))
print("when k = 5, the accuracy score for training data is:", knn_5.score(X_train, y_train))
print("when k = 5, the precision score is: ", precision_score(y_test, y_predict))
print("when k = 5, the recall score is: ", recall_score(y_test, y_predict))

a = precision_score(y_test, y_predict)
b = recall_score(y_test, y_predict)
print("when k = 5, the f1-score is: ", 2 * a * b / (a + b))
