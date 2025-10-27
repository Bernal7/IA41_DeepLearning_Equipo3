import numpy as np

#3 entradas
x1 = np.array([1.0, 2.0, 3.0])
x2 = np.array([0.5, 1.5, 2.5])

#1ra neurona oculta
w1 = np.array([0.2, -0.4, 0.1])
b1 = 0.3
h1 = np.tanh(np.dot(x1, w1) + b1)

#2da neurona oculta
w2 = np.array([-0.2, 0.4, -0.1])
b2 = -0.3
h2 = np.tanh(np.dot(x2, w2) + b2)

#1 neurona de salida
h = np.array([h1, h2])
w = np.array([0.6, -0.6])
b = -0.5
y = np.tanh(np.dot(h, w) + b)

print("Output:", y)