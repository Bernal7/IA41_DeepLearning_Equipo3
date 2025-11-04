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

# Primera capa oculta

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
match opt:
    case 1:
        Y = tf.nn.relu(y_ws)
    case 2:
        Y = tf.nn.sigmoid(y_ws)
    case 3:
        Y = tf.nn.tanh(y_ws)

# Mostrar salida
print("\nSalida Y:\n", Y)

x_linspace = np.linspace(0, 10, 100)

match opt:
    case 1:
        y_linspace = tf.nn.relu(x_linspace)
        lbl="ReLU"
    case 2:
        y_linspace = tf.nn.sigmoid(x_linspace)
        lbl="Sigmoid"
    case 3:
        y_linspace = tf.nn.tanh(x_linspace)
        lbl="Tanh"

plt.plot(x_linspace, y_linspace, label=lbl)

# Graficar puntos de Y (aplanados) usando índices como x
# .numpy() → convierte el tensor a un array de NumPy.
# .flatten() → convierte la matriz 2D (2,3) en un vector 1D:
Y_points = Y.numpy().flatten()

# len(Y_points) = número de elementos en este vector 1D (6 en este caso).
# np.arange(n) → genera un array [0, 1, 2, ..., n-1]:
x_indices = np.arange(len(Y_points))  # 0,1,2,... hasta 5 en este caso

plt.scatter(x_indices, Y_points, color="red", zorder=10, label=f"points in {lbl} func")

plt.title(f"{lbl} function")
plt.xlabel("index of output")
plt.ylabel(f"{lbl} output")
plt.legend()
plt.grid(True)
plt.show()
