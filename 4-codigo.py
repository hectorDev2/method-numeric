import numpy as np
    
    # Definición de la función
def f(x):
        return np.tan(x / 3)
    
    # Definición de la derivada analítica de la función
def df_exact(x):
    return (1/3) * (1 / np.cos(x / 3)**2)
    
# Punto donde se evalúa la derivada
x = 3
# Tamaño del paso
h = 0.1

# Aproximación por diferencia dividida hacia adelante
df_forward = (f(x + h) - f(x)) / h

# Aproximación por diferencia dividida hacia atrás
df_backward = (f(x) - f(x - h)) / h

# Aproximación por diferencia dividida central
df_central = (f(x + h) - f(x - h)) / (2 * h)

# Valor de la derivada analítica
df_analytic = df_exact(x)

# Cálculo del error relativo porcentual verdadero para cada aproximación
epsilon_t_forward = np.abs((df_analytic - df_forward) / df_analytic) * 100
epsilon_t_backward = np.abs((df_analytic - df_backward) / df_analytic) * 100
epsilon_t_central = np.abs((df_analytic - df_central) / df_analytic) * 100

# Imprimir los resultados
print(f"Punto x = {x}")
print(f"Tamaño del paso h = {h}\n")

print("Aproximaciones por diferencias divididas:")
print(f"  Hacia adelante: f'(x) ≈ {df_forward:.6f}, Error (|εt|%): {epsilon_t_forward:.2f}%")
print(f"  Hacia atrás:   f'(x) ≈ {df_backward:.6f}, Error (|εt|%): {epsilon_t_backward:.2f}%")
print(f"  Central:       f'(x) ≈ {df_central:.6f}, Error (|εt|%): {epsilon_t_central:.2f}%")

print(f"\nSolución analítica: f'(x) = {df_analytic:.6f}")