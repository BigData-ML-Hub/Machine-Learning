# Week 3: Maximum Margin Classification

## 1. Introduction to Maximum Margin Classification

**Definition**: Maximum margin classification aims to find a decision boundary that not only separates classes but does so with the **largest possible margin** between the boundary and any data point.

- **Margin**: The distance between the decision boundary and the closest data points from either class.
- **Objective**: Maximize this margin to enhance the classifier's generalization ability.

---

## 2. Concept of Linear Separability

A dataset is **linearly separable** if there exists a hyperplane that can perfectly separate the data points of different classes.

- **Hyperplane Equation**: $ w^T x + b = 0 $
  - $ w $: Weight vector (normal to the hyperplane)
  - $ x $: Input feature vector
  - $ b $: Bias term

For a data point $ (x_i, y_i) $:
- If $ y_i = 1 $, it belongs to the positive class.
- If $ y_i = -1 $, it belongs to the negative class.

A correct classification requires:
$$ y_i (w^T x_i + b) > 0 $$

---

## 3. Defining the Margin

The **functional margin** of a data point $ (x_i, y_i) $ with respect to a hyperplane $ (w, b) $ is:
$$ \gamma_i = y_i (w^T x_i + b) $$

The **geometric margin**, which considers the norm of $ w $, is:
$$ \hat{\gamma}_i = \frac{\gamma_i}{\|w\|} = \frac{y_i (w^T x_i + b)}{\|w\|} $$

The **margin** of the classifier is the smallest geometric margin among all data points:
$$ \hat{\gamma} = \min_{i} \hat{\gamma}_i $$

---

## 4. Optimization Problem for Maximum Margin

To find the hyperplane with the maximum margin, we solve the following optimization problem:

**Objective**:
$$ \max_{w, b} \hat{\gamma} $$

**Subject to**:
$$ y_i (w^T x_i + b) \geq \hat{\gamma}, \quad \forall i $$

By scaling $ w $ and $ b $, we can set $ \hat{\gamma} = 1 $, leading to the equivalent problem:

**Objective**:
$$ \min_{w, b} \frac{1}{2} \|w\|^2 $$

**Subject to**:
$$ y_i (w^T x_i + b) \geq 1, \quad \forall i $$

This is a **convex quadratic optimization problem** with linear constraints.

---

## 5. Lagrangian and Dual Formulation

To solve the above problem, we introduce Lagrange multipliers $ \alpha_i \geq 0 $ for each constraint and form the Lagrangian:

$$ L(w, b, \alpha) = \frac{1}{2} \|w\|^2 - \sum_{i} \alpha_i [y_i (w^T x_i + b) - 1] $$

By setting the derivatives of $ L $ with respect to $ w $ and $ b $ to zero, we derive the **dual problem**:

**Objective**:
$$ \max_{\alpha} \sum_{i} \alpha_i - \frac{1}{2} \sum_{i, j} \alpha_i \alpha_j y_i y_j x_i^T x_j $$

**Subject to**:
- $ \sum_{i} \alpha_i y_i = 0 $
- $ \alpha_i \geq 0, \quad \forall i $

Solving this dual problem yields the optimal $ \alpha $ values, from which we can compute $ w $ and $ b $.

---

## 6. Support Vectors

**Support vectors** are the data points that lie exactly on the margin boundaries, i.e., they satisfy:

$$ y_i (w^T x_i + b) = 1 $$

These points are critical because:

- They define the position of the decision boundary.
- The optimal hyperplane depends only on these points; other data points do not influence it.

---

## 7. Summary

- **Maximum margin classifiers** seek the hyperplane that separates classes with the largest margin.
- The problem is formulated as a convex optimization task, solvable via the dual formulation using Lagrange multipliers.
- **Support vectors** are the key data points that determine the optimal decision boundary.

---
