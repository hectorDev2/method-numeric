# Constantes dadas en el problema
K = 9e9  # N*m^2/C^2
Q = 2e-5  # C
q = 2e-5  # C
a = 0.9   # m
F_objetivo = 1.25  # N

# Definimos la función f(x) = F(x) - 1.25
def f(x):
    return (K * q * Q * x) / ((x**2 + a**2)**(3/2)) - F_objetivo

# Método de falsa posición (Regula Falsi)
def falsa_posicion(f, x0, x1, tol=0.001, max_iter=100):
    f0 = f(x0)
    f1 = f(x1)
    for i in range(max_iter):
        x2 = x1 - f1 * (x0 - x1) / (f0 - f1)
        f2 = f(x2)
        error = abs((x1 - x0) / x2) * 100
        if abs(f2) < 1e-6 or error < tol:
            return x2, i + 1, error
        if f0 * f2 < 0:
            x1 = x2
            f1 = f2
        else:
            x0 = x2
            f0 = f2
    return x2, max_iter, error  # Si no converge

# Ejecutamos el método con el intervalo [1, 1.5]
x_sol, iterations, final_error = falsa_posicion(f, 1, 1.5, tol=0.1)
x_sol, iterations, final_error
