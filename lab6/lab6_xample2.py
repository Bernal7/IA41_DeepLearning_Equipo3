"""

    * Implementar un programa de redes neuronales el cual contenga lo siguiente:

        * 3 Vectores de entrada con 3 valores cada uno.
        * 1 Matriz De Pesos con 3 Valores Para Cada Vector.
        * 3 Valores De Bias (Sesgo) Para Cada Vector.
        * Obtener la representación del programa en razón de la expresión matricial es decir: R1→R1→R1→R1 por ejemplo.
        * Obtener la representación utilizando NN-SVG y TensorFlowPlayGround.
        * Para "las 2 capas ocultas" tienen libertad de implementación de funciones de activación (siempre y cuando cumpla con la arquitectura esperada del programa".

    * 1 PDF por equipo, 1 commit y 1 conclusión por miembro.

"""

import numpy as np

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

x = np.array([
    [ 0.5, -1, -1.75 ], # Primer Vector de entradas
    [ -1.0, 2.3, 0.25], # Segundo ... ... ...
    [ -0.1, 0.45, 1.15] # Tercer ... ... ...
])

w = np.random.rand(3, 3)
w1 = np.random.rand(3, 3)
w2 = np.random.rand(3, 3)

b = np.random.rand(1, 3)
b1 = np.random.rand(1, 3)
b2 = np.random.rand(1, 3)

h1 = relu(np.dot(x, w1) + b1)
h2 = sigmoid(np.dot(x, w2) + b2)
output = tanh(np.dot(np.array([h1, h2]), w) + b)

print("Output de la red neuronal:")
print(output)