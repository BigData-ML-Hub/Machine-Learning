# Week 2: Logistic Regression

## 1. Introduction to Logistic Regression

**Definition**: Logistic Regression is a classification algorithm used to predict the probability that a given input belongs to a particular class.
It is particularly suited for binary classification problems.

Unlike linear regression which outputs continuous values, logistic regression outputs probabilities that are mapped to class labels (e.g., 0 or 1).

---

## 2. The Sigmoid Function

**Purpose**: To map any real-valued number into the range (0, 1), converting the output of a linear model into a probability.

### Formula:
$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Where $ z = w^T x + b $

- $ w $ = weight vector
- $ x $ = input vector
- $ b $ = bias term
- $ \sigma(z) $ = predicted probability (confidence score)

---

## 3. Decision Boundary

The decision boundary is defined where the predicted probability is 0.5 (i.e., $ \sigma(z) = 0.5 $).

Since:
$$
\sigma(z) = 0.5 \iff z = 0 \iff w^T x + b = 0
$$

This equation represents the linear decision boundary that separates the classes.

---

## 4. Loss Function: Cross-Entropy Loss

**Why not use MSE?**
Mean Squared Error doesn't work well for classification tasks due to the sigmoid's non-linearity. Instead, **Cross-Entropy Loss** is used.

### Formula:
$$
L(y, \hat{y}) = -[y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})]
$$

Where:
- $ y $ = true label (0 or 1)
- $ \hat{y} $ = predicted probability

---

## 5. Training via Gradient Descent

To minimize the cross-entropy loss, we use **gradient descent**.

### Gradient of the Loss w.r.t. Weights:
$$
\frac{\partial L}{\partial w} = (\hat{y} - y) \cdot x
$$

### Update Rule:
$$
w := w - \eta \cdot \frac{\partial L}{\partial w}
$$
$$
b := b - \eta \cdot (\hat{y} - y)
$$

Where $ \eta $ is the learning rate.

---

## 6. Multiclass Logistic Regression (Softmax)

When there are more than two classes, use **Softmax Regression** (a.k.a. Multinomial Logistic Regression).

### Softmax Function:
$$
P(y = k \mid x) = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}
$$

Where:
- $ z_k = w_k^T x + b_k $ for each class $ k $
- $ K $ = number of classes

---

## 7. Summary

- Logistic Regression is used for binary (and extended to multiclass) classification tasks.
- Uses the sigmoid (or softmax) function to predict probabilities.
- Cross-entropy loss guides the optimization.
- Training is performed via gradient descent.

---

**Tip**: Visualize the sigmoid curve to understand how small/large values of $ z $ affect the prediction confidence.