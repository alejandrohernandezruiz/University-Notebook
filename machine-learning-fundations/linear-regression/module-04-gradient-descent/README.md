# Module 4 — Gradient Descent

This module introduces **Gradient Descent**, an iterative optimization algorithm that allows Machine Learning models to find good parameter values without relying on a direct closed-form solution.

After studying Linear Regression through the **Normal Equation**, I moved from solving an optimization problem directly to understanding how its solution can be approached **step by step using Calculus and Optimization**.

The main goal of this module was to understand how the **gradient**, the **cost function**, and the **learning rate** work together to progressively improve a model.

## What I studied

* Optimization and cost functions
* Parameters and parameter vectors
* Gradients and partial derivatives
* Learning rate
* Iterations and convergence
* Batch Gradient Descent
* Gradient Descent for Linear Regression
* Vectorized matrix operations
* Feature scaling
* Cost history and convergence analysis
* Relationship between Gradient Descent and the Normal Equation

The central idea is to update the parameters in the direction that decreases the cost:

```text
θ ← θ - α∇J(θ)
```

For Linear Regression, the gradient can be written in matrix form as:

```text
∇J(θ) = (1/m)Xᵀ(Xθ - y)
```

This allows the parameters to be updated using the entire training dataset at each iteration.

## My approach

As in the previous modules, I first studied the mathematical foundations on paper before implementing them in Python.

I started with a simple mathematical function to understand the intuition behind descending along a gradient. I then applied the same idea to **Simple Linear Regression** and finally to **Multiple Linear Regression using the Design Matrix**.

The implementation uses **NumPy and vectorized matrix operations**, keeping the mathematics visible rather than hiding the optimization process behind a Machine Learning library.

I also experimented with different learning rates and feature scaling to understand their effect on convergence.

Finally, I compared the parameters obtained through Gradient Descent with those obtained from the **Normal Equation**, connecting the two approaches as different ways of solving the same optimization problem.

## 📓 Handwritten Notes

These are the handwritten notes I made while studying Gradient Descent, optimization, and its application to Linear Regression.

[View my handwritten notes](notes.md)

## 💻 Jupyter Notebook

[Open the Jupyter Notebook](../module-04-gradient-descent/gradient_descent_explanation/gradient_descent_explanation.ipynb)

---

**Previous:** [Multiple Linear Regression](../module-03-multiple-linear-regression/)

**Next:** Coming soon → [Logistic Regression](/machine-learning-fundations/logistic-regression/)
