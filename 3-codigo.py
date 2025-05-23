import numpy as np

# Datos de la tabla
x_data = np.array([1, 1.5, 1.6, 2.5])
fx_data = np.array([0.6767, 0.3734, 0.3261, 0.08422])

# Función verdadera y su derivada
def f(x):
    return 5 * x * np.exp(-2 * x)

def df_exact(x):
    return 5 * np.exp(-2 * x) - 10 * x * np.exp(-2 * x)

# Estimar la primera derivada usando diferencias finitas (adelante, atrás y central donde sea posible)
df_estimated = np.zeros_like(fx_data, dtype=float)

# Diferencia hacia adelante (para el primer punto)
h = x_data[1] - x_data[0]
df_estimated[0] = (fx_data[1] - fx_data[0]) / h

# Diferencia central (para los puntos intermedios)
for i in range(1, len(x_data) - 1):
    h_forward = x_data[i+1] - x_data[i]
    h_backward = x_data[i] - x_data[i-1]
    df_estimated[i] = (fx_data[i+1] - fx_data[i-1]) / (h_forward + h_backward)

# Diferencia hacia atrás (para el último punto)
h = x_data[-1] - x_data[-2]
df_estimated[-1] = (fx_data[-1] - fx_data[-2]) / h

# Calcular las derivadas verdaderas
df_true = df_exact(x_data)

# Calcular el error relativo porcentual verdadero (εt)
epsilon_t = np.abs((df_true - df_estimated) / df_true) * 100

# Imprimir los resultados
print("x\t f(x)\t f'(x)_estimada\t f'(x)_verdadera\t |εt| (%)")
print("-------------------------------------------------------------------------")
for i in range(len(x_data)):
    print(f"{x_data[i]:.1f}\t {fx_data[i]:.5f}\t {df_estimated[i]:.5f}\t\t {df_true[i]:.5f}\t\t {epsilon_t[i]:.2f}")