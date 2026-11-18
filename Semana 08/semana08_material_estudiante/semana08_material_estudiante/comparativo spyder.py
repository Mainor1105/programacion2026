import numpy as np

# 1. Crear matriz de 3x3 con ceros
matriz = np.zeros((3, 3))

# 2. Cambiar la diagonal por el número 5
np.fill_diagonal(matriz, 5)

# 3. En VS Code estás obligado a programar la salida visual en la consola
print("Resultado de la matriz:")
print("-" * 25)

for fila in matriz:
    # Formatear cada número para que se vea limpio sin decimales feos
    fila_formateada = "  ".join(f"{int(num)}" for num in fila)
    print(f"|  {fila_formateada}  |")

print("-" * 25)
