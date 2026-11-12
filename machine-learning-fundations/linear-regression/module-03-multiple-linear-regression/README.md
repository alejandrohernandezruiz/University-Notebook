# Module 3 — Multiple Linear Regression

This module is where I moved from **Simple Linear Regression** to **Multiple Linear Regression**.

Instead of using only one feature to predict a target, I started working with several features at the same time. This introduced me to a much more important mathematical tool for Machine Learning: **Linear Algebra**.

The main goal of this module was to understand how a regression problem can be written using vectors and matrices, and how the **Normal Equation** can be derived from the Least Squares method.

## What I studied

* Multiple Linear Regression
* Model parameters
* The Design Matrix
* Bias / Intercept
* Matrix notation
* Vector and matrix dimensions
* Overdetermined systems
* Least Squares
* Residuals
* Orthogonality
* Geometric interpretation
* The Normal Equation

The central idea can be written as:

```text
ŷ = Xβ
```

where `X` is the Design Matrix and `β` contains the model parameters.

From the Least Squares approach, the parameters can be obtained using the Normal Equation:

```text
β = (XᵀX)⁻¹Xᵀy
```

## My approach

As with the previous modules, I first worked through the mathematical ideas on paper.

I wanted to understand what the matrices represent, why the Design Matrix is constructed the way it is, and why the Least Squares solution leads to the Normal Equation.

After understanding the mathematics, I moved to Python and implemented the method using matrix operations.

The goal is not to treat Linear Regression as a black box, but to understand what is happening underneath the model.

## 📓 Handwritten Notes

These are the handwritten notes I made while studying Multiple Linear Regression and the mathematical foundations behind the Normal Equation.

[View my handwritten notes](notes.md)

## 💻 Jupyter Notebook

[Open the Jupyter Notebook](multiple_linear_regression.ipynb)

---

**Previous:** [Model Evaluation and Residuals](../module-02-model-evaluation/)

**Next:** Gradient Descent →
