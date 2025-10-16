import time
import numpy as np
import math
import matplotlib.pyplot as plt

#!Entradas de la funcion de mi neurona
inputs = np.array([1.0, 2.0, 3.0])

#todo: assign weigh for each on input
weights = np.array([0.2, 0.5, 0.3])

#?Bias: (ajustar el valor de la salida)
bias = 0.4

#todo: agregar prints "entradas, pesos, bias y numpy.tanh()"
out = inputs.copy()
np.tanh(inputs, out=out, where=True)

#!obtener la suma ponderada
weighted_sum = np.dot(inputs, weights) + bias

print("Entradas: ", inputs)
print("Pesos: ", weights)
print("Bias: ", bias)
print("Resultado de tanh: ", out)
print("Suma ponderada: ", weighted_sum)
print("Resultado de salida de activacion (tanh): ", np.tanh(weighted_sum))

x = np.linspace(-5, 5, 100)
y = np.tanh(x)

plt.plot(x, y)
plt.title("Función de Activación Tangente Hiperbólica (tanh)")
plt.xlabel("Entrada")
plt.ylabel("Salida tanh(x)")
plt.grid(True)
plt.show()