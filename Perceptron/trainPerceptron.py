import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from Perceptron import Perceptron

def accuracy(y_test, y_pred):
    acc = np.sum(y_test==y_pred)/len(y_test)
    return acc

X,y = datasets.make_blobs(n_samples=150, n_features=2, 
                          centers=2, cluster_std=1.05, random_state=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

clf = Perceptron()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print(f"Accuracy: {accuracy(y_test, predictions)}")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(X_train[:,0], X_train[:,1], marker="o", c=y_train)

x0_1 = np.amin(X_train[:,0])
x0_2 = np.amax(X_train[:,0])

x1_1 = (-clf.weights[0] * x0_1 - clf.bias) / clf.weights[1]
x1_2 = (-clf.weights[0] * x0_2 - clf.bias) / clf.weights[1]

ax.plot([x0_1, x0_2], [x1_1, x1_2], "k")

ymin = np.amin(X_train[:,1])
ymax = np.amax(X_train[:,1])
ax.set_ylim([ymin-3, ymax+3])

plt.show()