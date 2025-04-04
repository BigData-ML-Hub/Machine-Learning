# Week 4: Classification Errors, Regularization, and Logistic Regression

## 1. Classification Errors

**Types of Errors**:
- **False Positives (Type I Error)**: Incorrectly predicting a positive class.
- **False Negatives (Type II Error)**: Incorrectly predicting a negative class.

**Metrics**:
- **Accuracy**: $ \frac{\text{Number of correct predictions}}{\text{Total number of predictions}} $
- **Precision**: $ \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} $
- **Recall**: $ \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}} $
- **F1 Score**: Harmonic mean of Precision and Recall.

## 2. Regularization

**Purpose**: To prevent overfitting by adding a penalty term to the loss function.

**Types**:
- **L1 Regularization (Lasso)**: Adds $ \lambda \sum |w_i| $ to the loss function.
- **L2 Regularization (Ridge)**: Adds $ \lambda \sum w_i^2 $ to the loss function.

**Effect**:
- L1 can shrink some weights to zero, leading to sparse models.
- L2 penalizes large weights but doesn't enforce sparsity.

## 3. Logistic Regression

**Recap**: Logistic regression models the probability that a given input belongs to a particular class using the sigmoid function.

**Decision Boundary**: Determined by the weights and bias; the set of points where the model predicts a 50% probability.

**Regularized Logistic Regression**: Incorporates regularization terms into the logistic loss function to prevent overfitting.

---

*For detailed explanations, refer to the MIT lecture notes on Classification Errors, Regularization, and Logistic Regression.*