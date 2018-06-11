import numpy as np
from sklearn import preprocessing

matriz_ejemplo = np.array([[2.1, 2.9, -1.3, 5.2],
			  [1.3, -3.8, 2.1, 4.3],
			  [-81.9, 2.4, -1.1, 0],
			  [4.1, -3.9, 2.5, 2.1]])

datos_normalizados_l1 = preprocessing.normalize(matriz_ejemplo, norm='l1')
datos_normalizados_l2 = preprocessing.normalize(matriz_ejemplo, norm='l2')
print("Datos con Normalización L1:\n", datos_normalizados_l1)
print("\nDatos con Normalización L2:\n", datos_normalizados_l2)
