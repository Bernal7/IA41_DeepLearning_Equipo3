import numpy as np

#3 entradas
x = np.array([1.0, 2.0, 3.0])

#1 neurona oculta
w1 = np.array([0.2, -0.4, 0.1])
b1 = 0.3
h = np.tanh(np.dot(x, w1) + b1)

#1 neurona de salida
w2 = 0.6
b2 = -0.5
y = np.tanh((w2 * h) + b2)

print("Output:", y)