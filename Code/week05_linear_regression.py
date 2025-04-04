import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate Sample Data
np.random.seed(42)
X = np.linspace(0, 10, 50).reshape(-1, 1)
y = 3 * X.flatten() + np.random.randn(50) * 2  # y = 3x + noise

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, label="True Data")
plt.plot(X, y_pred, color="red", label="Linear Fit")
plt.legend()
plt.show()
