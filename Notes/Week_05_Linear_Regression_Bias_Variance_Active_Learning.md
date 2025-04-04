# Week 5: Linear Regression, Estimator Bias and Variance, Active Learning

## 1. Linear Regression

**Objective**: Model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.

**Equation**: $ y = w^T x + b $

**Assumptions**:
- Linearity: The relationship between the predictors and the outcome is linear.
- Independence: Observations are independent of each other.
- Homoscedasticity: Constant variance of errors.
- Normality: Errors are normally distributed.

## 2. Bias-Variance Tradeoff

**Bias**: Error introduced by approximating a real-world problem by a simplified model.

**Variance**: Error introduced by the model's sensitivity to small fluctuations in the training set.

**Tradeoff**:
- High bias can cause underfitting.
- High variance can cause overfitting.
- The goal is to find a balance that minimizes total error.

## 3. Active Learning

**Concept**: A learning algorithm can achieve greater accuracy with fewer training labels if it is allowed to choose the data from which it learns.

**Strategies**:
- **Uncertainty Sampling**: Selects the samples for which the current model is least certain.
- **Query-by-Committee**: Maintains a committee of models and selects samples about which the committee members disagree the most.

---

*For detailed explanations, refer to the MIT lecture notes on Linear Regression, Estimator Bias and Variance, and Active Learning.*