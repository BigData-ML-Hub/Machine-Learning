import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)

        for _ in range(self.epochs):
            for i, x_i in enumerate(X):
                update = self.lr * (y[i] - self.predict(x_i))
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        return np.where(np.dot(X, self.weights) + self.bias >= 0, 1, 0)

# Example Usage
X = np.array([[2, 3], [1, 1], [2, 2], [3, 1]])
y = np.array([1, 0, 1, 0])  # Binary classification labels

model = Perceptron()
model.fit(X, y)
print("Predictions:", model.predict(X))
