# Week 7: Kernel Regression, Kernels

## 1. Kernel Regression

**Concept**: A non-parametric technique that uses kernels to weigh nearby training instances when making predictions.

**Nadaraya-Watson Estimator**:
$$ \hat{f}(x) = \frac{\sum_{i=1}^{n} K(x, x_i) y_i}{\sum_{i=1}^{n} K(x, x_i)} $$
Where $ K $ is the kernel function.

**Bandwidth Selection**: Determines the width of the kernel function; a critical parameter that controls the smoothness of the prediction.

## 2. Kernels (Continued)

**Properties**:
- **Symmetry**: $ K(x, y) = K(y, x) $
- **Positive Semi-Definiteness**: For any set of points $ \{x_1, ..., x_n\} $, the kernel matrix $ K $ with entries $ K_{ij} = K(x_i, x_j) $ is positive semi-definite.

**Mercer's Theorem**: Provides conditions under which a function can be used as a kernel, ensuring that the associated kernel matrix is positive semi-definite.

---

*For detailed explanations, refer to the MIT lecture notes on Kernel Regression and Kernels.*