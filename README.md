# University-Notebook 📚

Welcome to my **University-Notebook**.

This repository is my personal space for learning, experimenting, making mistakes, and building a solid understanding of the subjects I study at university.

I don't want this to be just a collection of finished projects or copied code. I want to preserve the **process behind the learning**.

My goal is simple:

> **Understand the theory first, master the mathematics behind it, and only then write the code.**

---

## 🧠 How I Learn

One thing that has become very important to me is learning with **paper and pen**.

Before programming something, I try to understand the idea mathematically. I write down the equations, derive formulas step by step, and explain them in my own words.

After that, I move to Python and reproduce what I have learned from scratch.

So, when possible, the learning process in this repository follows this lifecycle:

```text
Theory
  ↓
Mathematics
  ↓
Handwritten Notes
  ↓
Python Implementation
  ↓
Experiments
  ↓
Conclusions
```

I scan my handwritten notes and include them here as images (`.png`). They are not meant to look perfect — they are raw, real artifacts of my learning process. 

I value **learning in public**, so I keep them here instead of hiding them away on my physical desk.

---

## 🗂️ Repository Structure (machine-learning-fundations)

The repository grows organically alongside my university progress. I avoid creating empty placeholder directories until I am actively working on them.

```text
University-Notebook/
├── machine-learning-fundations/
│   │
│   ├── linear-regression/
│   │   ├── module-01-simple-linear-regression/
│   │   │   ├── notes.md
│   │   │   ├── page-01.png
│   │   │   ├── page-02.png
│   │   │   ├── README.md
│   │   │   ├── simple_linear_regression.ipynb
│   │   │   └── students_data.csv
│   │   │
│   │   ├── module-02-model-evaluation/
│   │   │   ├── model_evaluation.ipynb
│   │   │   ├── notes.md
│   │   │   ├── page-02.png
│   │   │   ├── README.md
│   │   │   └── studentssss_data.csv
│   │   │
│   │   ├── module-03-multiple-linear-regression/
│   │   │   ├── images/
│   │   │   ├── multiple_linear_regression.ipynb
│   │   │   ├── notes.md
│   │   │   └── README.md
│   │   │
│   │   ├── module-04-gradient-descent/
│   │   │   ├── gradient_descent_explanation/
│   │   │   │   └── gradient_descent_explanation.ipynb
│   │   │   ├── gradient_descent_simple/
│   │   │   │   ├── gradient_descent_simple.ipynb
│   │   │   │   └── Salary_Data.csv
│   │   │   ├── images/
│   │   │   ├── notes.md
│   │   │   └── README.md
│   │   └── README.md
│   │
│   └── logistic-regression/
│
├── projects/
├── resources/
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🤖 Machine Learning Foundations

This section contains the mathematical, theoretical, and practical implementations of core machine learning algorithms. I treat no algorithm as a black box; I aim to explore the underlying matrix calculus and optimization techniques that make them work.

```text
Linear Algebra ──────┐
                     │
                     ├──→ Robust Machine Learning Models
                     │
Calculus ────────────┘
```

### 📈 Linear Regression

#### [Module 01: Simple Linear Regression](./machine-learning-fundations/linear-regression/module-01-simple-linear-regression/)
* **Focus:** Understanding line-fitting mechanics, independent/dependent variables, and mapping basic statistical foundations.
* **Hands-on:** Scratch Python implementations paired with initial data tests (`students_data.csv`).

#### [Module 02: Model Evaluation](./machine-learning-fundations/linear-regression/module-02-model-evaluation/)
* **Focus:** How do we know a model is good? Residual analysis, Mean Squared Error (MSE), R-squared (\(R^2\)), and tracking error metrics.
* **Hands-on:** Evaluating model bounds using validation loops over mock university student datasets.

#### [Module 03: Multiple Linear Regression](./machine-learning-fundations/linear-regression/module-03-multiple-linear-regression/)
* **Focus:** Moving from 2D space to multi-dimensional feature spaces using **Linear Algebra** and matrix forms.
* **Key Topics:** Design Matrix, transpose operations, matrix inverses, and parameter estimation.
* **The Math:** Deriving and implementing the **Normal Equation** from scratch using raw NumPy:
  ```python
  theta = np.linalg.inv(X.T @ X) @ X.T @ y
  ```

#### [Module 04: Gradient Descent](./machine-learning-fundations/linear-regression/module-04-gradient-descent/)
* **Focus:** Optimization using **Calculus**. Understanding how models learn iteratively when matrix inversion becomes computationally expensive.
* **Key Topics:** Cost functions, partial derivatives, loss landscapes, learning rates (\(\alpha\)), parameter updates, and global convergence.
* **Hands-on:** Pure algorithmic breakdown (`gradient_descent_simple.ipynb`) benchmarked on real-world engineering metrics (`Salary_Data.csv`).

---

# 🛠️ Projects & Resources

* **[Projects/](./projects/):** Dedicated space for end-to-end applications where theory intersects with practical engineering problems. As my knowledge stack scales, these will encompass larger pipeline architectures.
* **[Resources/](./resources/):** A curated reference collection of clean documentation, academic papers, books, and specific math proofs that helped me solve complex bottlenecks.

---

# 💻 Technology Stack & Tools

* **Core Language:** Python 🐍
* **Data Engineering & Math:** NumPy, Pandas
* **Data Visualization:** Matplotlib
* **Environments:** Jupyter Notebooks, VS Code
* **Version Control:** Git & GitHub

When studying fundamentals, I intentionally bypass high-level abstractions (like Scikit-Learn) until I can cleanly implement the math manually. High-level frameworks are amazing for industry production, but understanding the underlying architecture is non-negotiable for true mastery.

---

# ✍️ Why Handwritten Notes?

Writing mathematics by hand forces me to slow down and internalize the logic. When analyzing an equation like \(\theta = (X^T X)^{-1} X^T y\), I want to know exactly what every dimension represents and why it minimizes our loss function. 

You will find scanned handwritten notebooks (`page-XX.png`) tucked neatly inside each module's directory. They are transparent windows into my actual problem-solving journey.

---

# 🌱 Learning in Public

This repository is bound to contain mistakes. Some explanations will evolve. Some code will be heavily refactored. Some mathematical definitions that I think I understand today will look completely different and vastly clearer six months from now.

I keep this repository public because engineering is an iterative journey. It serves as a living proof of my growth, technical adaptability, and dedication to deep technical foundations.

# 🛠️ Projects and Resources Portfolio

* **[📂 Projects/](./projects/):** A direct index to my independent production repositories. This is where theory becomes real software through engineering applications, data pipelines, and optimization projects.
* **[📂 Resources/](./resources/):** My quick-reference library. It contains links to official documentation (`NumPy`, `Pandas`), freely available theoretical books (`ISLR`), and mathematical reference sheets for solving algorithmic bottlenecks.

