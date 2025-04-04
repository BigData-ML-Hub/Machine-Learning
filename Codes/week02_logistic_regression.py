import numpy as np
from sklearn.linear_model import LogisticRegression

# Example Data
X = np.array([[2, 3], [1, 1], [2, 2], [3, 1]])
y = np.array([1, 0, 1, 0])  # Binary labels

# Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Predictions
print("Predictions:", model.predict(X))
print("Probabilities:", model.predict_proba(X))
