
# Definimos la función f(t) = c(t) - 15
def f(t):
    return 75 * np.exp(-1.5 * t) + 20 * np.exp(-0.075 * t) - 15

# Derivada de la función f(t)
def f_prime(t):
    return -1.5 * 75 * np.exp(-1.5 * t) - 0.075 * 20 * np.exp(-0.075 * t)

# Método de Newton-Raphson
def newton_raphson(f, f_prime, t0, tol=0.001, max_iter=100):
    t = t0
    for i in range(max_iter):
        t_new = t - f(t) / f_prime(t)
        error = abs((t_new - t) / t_new) * 100
        if error < tol:
            return t_new, i + 1, error
        t = t_new
    return t, max_iter, error  # Si no converge

# Ejecutamos el método con t0 = 6 y tolerancia de 0.1%
t_sol, iterations, final_error = newton_raphson(f, f_prime, t0=6, tol=0.1)
t_sol, iterations, final_error
