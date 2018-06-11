<!--
.. title: Preprocesando datos para Machine Learning
.. slug: preprocesando-datos-para-machine-learning
.. date: 2018-06-11 02:30:15 UTC-03:00
.. tags: python, machine learning, scikit, numpy, scipy, artificial inteligence, inteligencia artificial, ai, ia, preprocessing
.. category: Programación
.. link: 
.. description: Cómo preprocesar datos para Machine Learning usando la librería scikit en Python
.. type: text
.. author: nespino
-->

A todos nos gustaría llegar a casa y que la cena esté lista. A los algoritmos de [Machine Learning](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico "¿Qué es Machine Learning?") también, por eso es que hoy vamos a dejarles cuatro recetas para que puedan alimentar en forma eficiente a sus procesos de entrenamiento.

Las recetas que repasaremos el día de hoy son:

* Binarización
* Eliminación del valor medio
* Escalando
* Normalización

> Cada caso puede requerir el uso de uno o más de estos métodos en forma combinada.

Para simplificarnos las tareas matemáticas, vamos a hacer uso de dos paquetes [Open Source](https://es.wikipedia.org/wiki/Software_libre_y_de_c%C3%B3digo_abierto "Diferencias entre Software Libre y Código Abierto") para desarrollos científicos:

* [Numpy](http://www.numpy.org/ "Numpy"), el cual se puede instalar junto a las de herramientas de [SciPy](https://www.scipy.org/install.html "¿Cómo instalar SciPy?")
* El paquete de aprendizaje de Machine Learning [scikit](http://scikit-learn.org/stable/install.html "Scikit Learn")

Ambos se pueden instalar fácilmente desde **pip** con los siguientes comandos:

> pip install scipy

> pip install scikit-learn

Primero vamos a importar las librerías necesarias y definir una matriz de ejemplo en numpy para usar en cada uno de los métodos que explicaremos a continuación

> import numpy as np

> from sklearn import preprocessing

>

> matriz_ejemplo = np.array([[2.3, 2.9, -1.3, 5.2],

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1.3, -3.8, 2.1, 4.3],

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-8.9, 2.4, -1.1, 0],

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4.1, -3.9, 2.5, 2.1]])


# Binarización 

Este método es comparable al que utilizan las entradas de las [Compuertas Lógicas](https://es.wikipedia.org/wiki/Puerta_l%C3%B3gica "Compuertas Lógicas") con las que están hechas todos nuestros dispositivos electrónicos, en el que, habiendo definido un valor de umbral, podemos separar a los datos que ingresan de manera que los menores a ese umbral correspondan a 0 (False) y los mayores correspondan a 1 (True). Vamos a transformar esos valores numéricos en valores booleanos, usando un umbral de 2.4 con la función Binarizer:

> matriz_binarizada = preprocessing.Binarizer(threshold=2.4).transform(matriz_ejemplo)

> print("Matriz binarizada:\n", matriz_binarizada)
 
y el resultado será:

> Matriz binarizada:

> &nbsp;&nbsp;[[0. 1. 0. 1.]

> &nbsp;&nbsp;[0. 0. 0. 1.]

> &nbsp;&nbsp;[0. 0. 0. 0.]

> &nbsp;&nbsp;[1. 0. 1. 0.]]

Observen que el segundo elemento de la tercer fila de la matriz de ejemplo es 2.4, y al binarizarlo con el umbral 2.4 se obtiene un 0 en la misma posición.

*Pueden encontrar el código completo de este método en el archivo de ejemplo <a href="/code/ai/binarizacion.py" download>binarizacion.py</a>.*

# Eliminación del valor medio

Este método es muy usado en preprocesamiento de datos para Machine Learning, con el cual se elimina el sesgo de las características en nuestro vector característico. La función que nos permite esta transformación se llama **scale** y es muy sencilla de usar. Para verificar los resultados paso a paso incluímos algunos **prints**.

> print("Matriz de ejemplo:")

> print(matriz_ejemplo)

> print("Promedio =", matriz_ejemplo.mean(axis=0))

> print("Desviación típica =", matriz_ejemplo.std(axis=0))

> &nbsp;

> promedio_eliminado = preprocessing.scale(matriz_ejemplo)

> print("\nMatriz procesada:")

> print(promedio_eliminado)

> print("Promedio =", promedio_eliminado.mean(axis=0))

> print("Desviación Típica =", promedio_eliminado.std(axis=0))

Lo que debería darnos como resultado:

> Matriz de ejemplo:

> &nbsp;[[ 2.1  2.9 -1.3  5.2]

> &nbsp;[ 1.3 -3.8  2.1  4.3]

> &nbsp;[-8.9  2.4 -1.1  0. ]

> &nbsp;[ 4.1 -3.9  2.5  2.1]]

> Promedio = [-0.35 -0.6   0.55  2.9 ]

> Desviación típica = [5.04058528 3.25499616 1.75712834 2.01866292]

> &nbsp;

> Matriz procesada:

> &nbsp;[[ 0.48605467  1.07527009 -1.05285423  1.13936803]

> &nbsp;[ 0.32734294 -0.98310408  0.88212111  0.69352837]

> &nbsp;[-1.69623159  0.92166007 -0.93903215 -1.43659447]

> &nbsp;[ 0.88283399 -1.01382608  1.10976527 -0.39630192]]

> Promedio = [ 0.00000000e+00  0.00000000e+00 -1.11022302e-16  4.16333634e-17]

> Desviación Típica = [1. 1. 1. 1.]

Como pueden observar el promedio en la matriz procesada está cerca de 0 y la desviación típica es 1.

*Pueden encontrar el código completo de este método en el archivo de ejemplo <a href="/code/ai/eliminar_valor_medio.py" download>eliminar_valor_medio.py</a>.*


# Escalando

Es posible que nuestro vector característico incluya valores extremadamente altos y/o extremadamente bajos, por eso es importante escalar esos valores para que nuestro algoritmo opere con valores cercanos, y así evitamos características con valores desorbitantes.

> datos_escalados = preprocessing.MinMaxScaler(feature_range=(0, 1))

> datos_escalados = datos_escalados.fit_transform(matriz_ejemplo)

> print("Datos escalados:\n", datos_escalados)

Podemos comprobar que cada fila fue escalada para que sus valores mínimos y máximos sean 0 y 1 respectivamente, y los demás se transformaron en forma proporcional:

> Datos escalados:

> &nbsp;[[0.84615385 1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]

> &nbsp;&nbsp;[0.78461538&nbsp; 0.01470588 0.89473684 0.82692308&nbsp;]

> &nbsp;&nbsp;[0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.92647059 0.05263158 0.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]

> &nbsp;&nbsp;[1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.40384615&nbsp;]]

*Pueden encontrar el código completo de este método en el archivo de ejemplo <a href="/code/ai/escalando.py" download>escalando.py</a>.*


# Normalización

La normalización se usa para modificar los valores en el vector característico y así poder medirlos en una escala común. Existen varios métodos para esto, así que vamos a presentarles los dos más comunes.

__Normalización L1__: Busca las menores desviaciones absolutas, y funciona asegurándose que la suma de los valores absolutos en cada fila sea 1.

__Normalización L2__: Busca los menores cuadrados, y funciona asegurándose que la suma de los cuadrados sea 1.

En general el método de Normalización L1 se considera más robusto que el de Normalización L2, porque el primero es más resistente a valores atípicos en los datos de origen. Es frecuente encontrar valores atípicos y no hay nada que podamos hacer al respecto, por eso buscamos técnicas que los ignoren de forma segura y efectiva durante los cálculos. En cambio, si los valores atípicos son importantes para el problema que estamos resolviendo, podríamos inclinarnos a usar la Normalización L2.

> datos_normalizados_l1 = preprocessing.normalize(matriz_ejemplo, norm='l1')

> datos_normalizados_l2 = preprocessing.normalize(matriz_ejemplo, norm='l2')

> print("Datos con Normalización L1:\n", datos_normalizados_l1)

> print("\nDatos con Normalización L2:\n", datos_normalizados_l2)

Usamos la función **normalize**, indicando el tipo de normalización, y así podremos apreciar la diferencia por pantalla:

> Datos con Normalización L1:

> [[ 0.1826087   0.25217391 -0.11304348  0.45217391]

> [ 0.11304348 -0.33043478  0.1826087   0.37391304]

> [-0.71774194  0.19354839 -0.08870968  0.        ]

> [ 0.32539683 -0.30952381  0.1984127   0.16666667]]

> &nbsp;

> Datos con Normalización L2:

> [[ 0.32578702  0.44989636 -0.20167768  0.80671072]

> [ 0.20808658 -0.60825309  0.33613986  0.68828639]

> [-0.95870891  0.25852824 -0.11849211  0.        ]

> [ 0.62758369 -0.59696986  0.38267298  0.32144531]]


*Pueden encontrar el código completo de este método en el archivo de ejemplo <a href="/code/ai/normalizacion.py" download>normalizacion.py</a>.*

Espero que con estos métodos le den un merecido banquete a sus algoritmos, y que tengan ustedes una deliciosa y nutritiva cena.


