# Numerical Methods in Python

This repository contains Python implementations of the numerical methods problems from the "Primer Examen de Métodos Numéricos" (First Numerical Methods Exam) dated 15/05/2025.

## Problems Solved

The following problems from the exam have been solved and implemented in Python:

1.  **Problem 1: Bacterial Concentration Decay**
    * Implemented the Newton-Raphson method to determine the time required for bacterial concentration to reduce to a specific level. [cite: 1]
    * Equation used:  $c=75e^{-1.5t}+20e^{-0.075t}$ [cite: 1]
    * Initial guess: $t_0 = 6$
    * Stopping criterion: 0.1%

2.  **Problem 2: Force Between Charged Ring and Point Charge**
    * Implemented the False Position method to find the distance x where the force between a charged ring and a point charge is 1.25 N. [cite: 2, 3, 4, 5]
    * Equation used: $F=K\frac{qQx}{(x^{2}+a^{2})^{\frac{3}{2}}}$  where $K=9\times10^{9}Nm^{2}/C^{2}$ [cite: 4]
    * Given values: $Q=2\times10^{-5}C$, $a=0.9$ m, $q =2\times10^{-5}C$ [cite: 2, 3]
    * Root finding interval: [1, 1.5]

3.  **Problem 3: Numerical Differentiation**
    * Calculated estimates of the first derivative for given data points. [cite: 5, 6]
    * Data points:
        * X: \[1, 1.5, 1.6, 2.5]
        * f(x): \[0.6767, 0.3734, 0.3261, 0.08422] [cite: 6]
    * Compared results with the true derivative of $f(x)=5xe^{-2x}$ and calculated the relative percentage error. [cite: 7]

4.  **Problem 4: Finite Difference Approximations**
    * Calculated forward, central, and backward difference approximations for the function $f(x)=tan(\frac{x}{3})$ at $x=3$ with $h=0.1$. [cite: 7, 8]
    * Compared the approximations with the analytical solution and calculated the relative percentage error. [cite: 8]

## Repository Structure
