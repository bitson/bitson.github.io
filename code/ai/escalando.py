import numpy as np
from sklearn import preprocessing

matriz_ejemplo = np.array([[2.1, 2.9, -1.3, 5.2],
			  [1.3, -3.8, 2.1, 4.3],
			  [-8.9, 2.4, -1.1, 0],
			  [4.1, -3.9, 2.5, 2.1]])

datos_escalados = preprocessing.MinMaxScaler(feature_range=(0, 1))
datos_escalados = datos_escalados.fit_transform(matriz_ejemplo)
print("Datos escalados:\n", datos_escalados)
