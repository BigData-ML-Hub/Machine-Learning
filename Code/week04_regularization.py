import numpy as np
from sklearn.linear_model import LogisticRegression

# Example Data
X = np.array([[2, 3], [1, 1], [2, 2], [3, 1]])
y = np.array([1, 0, 1, 0])

# L2 Regularization (Ridge)
model = LogisticRegression(C=1.0, penalty='l2')
model.fit(X, y)

print("L2 Regularized Coefficients:", model.coef_)
