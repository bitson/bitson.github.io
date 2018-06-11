import numpy as np
from sklearn import preprocessing

matriz_ejemplo = np.array([[2.1, 2.9, -1.3, 5.2],
			  [1.3, -3.8, 2.1, 4.3],
			  [-8.9, 2.4, -1.1, 0],
			  [4.1, -3.9, 2.5, 2.1]])

print("Matriz de ejemplo:")
print(matriz_ejemplo)
print("Promedio =", matriz_ejemplo.mean(axis=0))
print("Desviación típica =", matriz_ejemplo.std(axis=0))

promedio_eliminado = preprocessing.scale(matriz_ejemplo)
print("\nMatriz procesada:")
print(promedio_eliminado)
print("Promedio =", promedio_eliminado.mean(axis=0))
print("Desviación Típica =", promedio_eliminado.std(axis=0))




