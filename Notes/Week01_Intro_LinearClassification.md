# Week 1: Introduction to Machine Learning

## 1. Introduction to Machine Learning
**Definition**: Machine Learning (ML) is a subset of artificial intelligence that enables systems to learn patterns from data and make decisions or predictions without being explicitly programmed.

---

## 2. Supervised vs. Unsupervised Learning

### Supervised Learning
The algorithm learns from **labeled data**, making predictions or decisions based on input-output pairs.  
 Examples: Classification, Regression

### Unsupervised Learning
The algorithm explores **unlabeled data** to find hidden patterns or intrinsic structures without predefined categories.  
 Examples: Clustering, Dimensionality Reduction

---

## 3. Linear Classification
**Concept**: Linear classifiers aim to separate data points of different classes using a **linear decision boundary (hyperplane)**.  
The goal is to find a hyperplane that best divides the dataset into distinct classes.

---

## 4. Perceptron Update Rule

### Perceptron Model
An early type of linear classifier that updates its weights based on misclassified examples.

### Update Rule
For each misclassified instance, update the weights \( w \) and bias \( b \) as follows:

w = w + y * x

b = b + y


Where:
- \( x \) = input vector  
- \( y \) = true label

---

## 5. Reinforcement Learning Basics

**Definition**: A type of learning where an **agent** interacts with an **environment** to achieve a goal, receiving feedback in the form of rewards or penalties.

### Key Elements:
- **Agent**: The learner or decision-maker  
- **Environment**: The system with which the agent interacts  
- **Actions**: Choices the agent can make  
- **Rewards**: Feedback from the environment based on the agent's actions
