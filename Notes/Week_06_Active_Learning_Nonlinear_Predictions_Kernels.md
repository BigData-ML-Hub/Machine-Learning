# Week 6: Active Learning (cont.), Non-linear Predictions, Kernels

## 1. Active Learning (Continued)

**Pool-Based Sampling**: The model selects the most informative samples from a large pool of unlabeled data to be labeled.

**Stream-Based Selective Sampling**: Each unlabeled instance is considered for labeling based on its informativeness as it arrives.

## 2. Non-linear Predictions

**Need for Non-linearity**: Real-world data often exhibits complex patterns that linear models cannot capture.

**Approaches**:
- **Polynomial Regression**: Extends linear regression by considering polynomial features of the input variables.
- **Neural Networks**: Utilize activation functions to introduce non-linearity.

## 3. Kernels

**Purpose**: Enable linear algorithms to learn non-linear patterns by mapping input features into higher-dimensional spaces.

**Kernel Trick**: Computes the inner product in the transformed space without explicitly performing the transformation.

**Common Kernels**:
- **Linear Kernel**: $ K(x, y) = x^T y $
- **Polynomial Kernel**: $ K(x, y) = (x^T y + c)^d $
- **Gaussian (RBF) Kernel**: $ K(x, y) = \exp(-\frac{\|x - y\|^2}{2\sigma^2}) $

---

*For detailed explanations, refer to the MIT lecture notes on Active Learning, Non-linear Predictions, and Kernels.*