import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Example Data
X = np.array([[1, 2], [2, 3], [3, 3], [4, 5], [5, 6], [6, 7]])
y = np.array([0, 0, 1, 1, 1, 0])

# Kernel SVM
model = SVC(kernel='rbf', C=1.0)
model.fit(X, y)

# Predictions
print("Predictions:", model.predict(X))

# Plot Decision Boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
plt.title("Kernel SVM Decision Boundary")
plt.show()
