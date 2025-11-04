import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

print("... Bienvenido ...\n")
print("Selecciona una función de activación para realizar las predicciones ...")
print("1) ReLU")
print("2) Sigmoid")
print("3) Tangente hiperbólica\n")

opt = int(input("Your Option: "))
print()

# Parámetros para generar valores aleatorios
min_val = 0
max_val = 1

# Capa de entrada (2 ejemplos, 3 features cada uno)

#tf.random.uniform ---> crea un tensor de 3x3 en un rango de valores establecidos  con un tipo de dato fijo

x1 = tf.random.uniform((3,), minval=min_val, maxval=max_val, dtype=tf.float32)
x2 = tf.random.uniform((3,), minval=min_val, maxval=max_val, dtype=tf.float32)

# .stack ---> toma varios tensores del mismo tamaño y los “apila” creando un nuevo eje.
X = tf.stack([x1, x2])  # forma (2,3), cada fila es un ejemplo

# Pesos y bias de la primera capa
w1 = tf.random.uniform((3, 3), minval=min_val, maxval=max_val, dtype=tf.float32)
b1 = tf.random.uniform((3,), minval=min_val, maxval=max_val, dtype=tf.float32)

# Primera capa oculta

# tf.matmul saca el producto punto
z_ws = tf.matmul(X, w1) + b1  # (2,3) * (3,3) = (2,3)

# Aplicar función de activación según la opción
match opt:
    case 1:
        z = tf.nn.relu(z_ws)
    case 2:
        z = tf.nn.sigmoid(z_ws)
    case 3:
        z = tf.nn.tanh(z_ws)

# Segunda capa (salida)
w2 = tf.random.uniform((3, 3), minval=min_val, maxval=max_val, dtype=tf.float32)
b2 = tf.random.uniform((3,), minval=min_val, maxval=max_val, dtype=tf.float32)

# tf.matmul saca el producto punto
y_ws = tf.matmul(z, w2) + b2  # (2,3) * (3,3) = (2,3)

# Aplicar función de activación según la opción
