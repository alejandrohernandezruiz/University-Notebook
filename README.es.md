[![English](https://img.shields.io/badge/Language-English-blue.svg)](./README.md)

# University-Notebook 📚

Bienvenido a mi **University-Notebook**.

Este repositorio es mi espacio personal para aprender, experimentar, cometer errores y construir una comprensión sólida de las asignaturas que estudio en la universidad. No quiero que esto sea simplemente una colección de proyectos terminados o código copiado. Quiero preservar el **proceso detrás del aprendizaje**.

Mi objetivo es sencillo:

> **Entender primero la teoría, dominar las matemáticas que hay detrás y, solo entonces, escribir el código.**

---

## 🧠 Cómo Aprendo

Algo que se ha vuelto muy importante para mí es aprender con **papel y boli**. Antes de programar nada, intento comprender la idea matemáticamente. Escribo las ecuaciones, derivo las fórmulas paso a paso y las explico con mis propias palabras. Después, paso a Python y reproduzco desde cero lo que he aprendido.

Por ello, siempre que es posible, el proceso de aprendizaje en este repositorio sigue este ciclo de vida:

```text
Teoría
  ↓
Matemáticas
  ↓
Apuntes a mano
  ↓
Implementación en Python
  ↓
Experimentos
  ↓
Conclusiones
```

Escaneo mis apuntes manuscritos y los incluyo aquí como imágenes (`.png`). No pretenden verse perfectos; son apuntes reales y sin filtros de mi proceso de aprendizaje. Valoro el **aprender en público** (*learning in public*), así que los guardo aquí en lugar de dejarlos escondidos en mi escritorio.

---

## 🗂️ Estructura del Repositorio (aquí solo muestro machine-learning-fundations)

El repositorio crece de forma orgánica a la par que mi progreso en la universidad. Evito crear directorios vacíos de relleno hasta que estoy trabajando activamente en ellos.

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
├── README.es.md
└── requirements.txt
```

---

# 🤖 Fundamentos de Machine Learning

Esta sección contiene las implementaciones matemáticas, teóricas y prácticas de los algoritmos fundamentales de *Machine Learning*. No trato ningún algoritmo como una caja negra; mi objetivo es explorar el cálculo matricial y las técnicas de optimización subyacentes que los hacen funcionar.

```text
Álgebra Lineal ──────┐
                     ├──→ Modelos Robustos de Machine Learning
Cálculo ─────────────┘
```

### 📈 Regresión Lineal

#### [Módulo 01: Regresión Lineal Simple](./machine-learning-fundations/linear-regression/module-01-simple-linear-regression/simple_linear_regression.ipynb)
* **Enfoque:** Comprender la mecánica del ajuste de rectas, las variables independientes/dependientes y mapear los fundamentos estadísticos básicos.
* **Práctica:** Implementaciones desde cero en Python acompañadas de pruebas iniciales con datos (`students_data.csv`).

#### [Módulo 02: Evaluación de Modelos](./machine-learning-fundations/linear-regression/module-02-model-evaluation/model_evaluation.ipynb)
* **Enfoque:** ¿Cómo sabemos si un modelo es bueno? Análisis de residuos, Error Cuadrático Medio (MSE), coeficiente de determinación ($R^2$) y seguimiento de métricas de error.
* **Práctica:** Evaluación de los límites del modelo mediante bucles de validación sobre conjuntos de datos simulados de estudiantes universitarios.

#### [Módulo 03: Regresión Lineal Múltiple](./machine-learning-fundations/linear-regression/module-03-multiple-linear-regression/multiple_linear_regression.ipynb)
* **Enfoque:** Pasar de un espacio 2D a espacios de características multidimensionales utilizando **Álgebra Lineal** y formas matriciales.
* **Temas clave:** Matriz de diseño, operaciones de transposición, matrices inversas y estimación de parámetros.
* **Las matemáticas:** Derivación e implementación de la **Ecuación Normal** desde cero utilizando NumPy puro:
  ```python
  theta = np.linalg.inv(X.T @ X) @ X.T @ y
  ```

#### [Módulo 04: Descenso del Gradiente](./machine-learning-fundations/linear-regression/module-04-gradient-descent/)
* **Enfoque:** Optimización mediante **Cálculo**. Comprender cómo aprenden los modelos de forma iterativa cuando la inversión de matrices se vuelve computacionalmente costosa.
* **Temas clave:** Funciones de coste, derivadas parciales, paisajes de pérdida (*loss landscapes*), tasas de aprendizaje ($\alpha$), actualización de parámetros y convergencia global.
* **Práctica:** Desglose algorítmico puro (`gradient_descent_simple.ipynb`) puesto a prueba con métricas reales de ingeniería (`Salary_Data.csv`).

---

# 🛠️ Proyectos y Recursos

* **[Projects/](./projects/):** Espacio dedicado a aplicaciones completas (*end-to-end*) donde la teoría se cruza con problemas prácticos de ingeniería. A medida que crezca mi base de conocimientos, abarcarán arquitecturas de *pipelines* más grandes.
* **[Resources/](./resources/):** Una colección seleccionada de documentación limpia, artículos académicos, libros y demostraciones matemáticas específicas que me han ayudado a resolver cuellos de botella complejos.

---

# 💻 Stack Tecnológico y Herramientas

* **Lenguaje principal:** Python 🐍
* **Ingeniería de datos y matemáticas:** NumPy, Pandas
* **Visualización de datos:** Matplotlib
* **Entornos:** Jupyter Notebooks, VS Code
* **Control de versiones:** Git y GitHub

Cuando estudio los fundamentos, evito intencionadamente las abstracciones de alto nivel (como Scikit-Learn) hasta que soy capaz de implementar las matemáticas manualmente de forma limpia. Los *frameworks* de alto nivel son excelentes para producción en la industria, pero comprender la arquitectura subyacente es innegociable para alcanzar un verdadero dominio.

---

# ✍️ ¿Por qué apuntes a mano?

Escribir matemáticas a mano me obliga a bajar el ritmo e interiorizar la lógica. Al analizar una ecuación como $\theta = (X^T X)^{-1} X^T y$, quiero saber exactamente qué representa cada dimensión y por qué minimiza nuestra función de pérdida.

Encontrarás cuadernos manuscritos escaneados (`page-XX.png`) guardados ordenadamente dentro del directorio de cada módulo. Son ventanas transparentes a mi proceso real de resolución de problemas.

---

# 🌱 Aprender en Público

Este repositorio inevitablemente contendrá errores. Algunas explicaciones evolucionarán. Parte del código será refactorizado en profundidad. Algunas definiciones matemáticas que hoy creo entender se verán completamente diferentes y mucho más claras dentro de seis meses.

Mantengo este repositorio público porque la ingeniería es un viaje iterativo. Sirve como una prueba viva de mi crecimiento, adaptabilidad técnica y dedicación a unos cimientos técnicos sólidos.

---

# 🛠️ Portafolio de Proyectos y Recursos

* **[📂 Projects/](./projects/):** Un índice directo a mis repositorios independientes en producción. Aquí es donde la teoría se convierte en software real mediante aplicaciones de ingeniería, *pipelines* de datos y proyectos de optimización.
* **[📂 Resources/](./resources/):** Mi biblioteca de consulta rápida. Contiene enlaces a documentación oficial (`NumPy`, `Pandas`), libros teóricos de acceso gratuito (`ISLR`) y hojas de referencia matemática para resolver cuellos de botella algorítmicos.