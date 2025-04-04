import numpy as np
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge

# Generate Sample Data
np.random.seed(42)
X = np.linspace(0, 10, 50).reshape(-1, 1)
y = np.sin(X).flatten() + np.random.randn(50) * 0.1  # Non-linear function

# Kernel Ridge Regression
model = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, label="True Data")
plt.plot(X, y_pred, color="red", label="Kernel Regression Fit")
plt.legend()
plt.show()
