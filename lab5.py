import numpy as np
import matplotlib.pyplot as plt

op = 0

# Solicitar al usuario que elija la función de activación valida
while op not in ['1', '2', '3']:
    print("Enter the operation: ")
    print("1) tanh")
    print("2) sigmoid")
    print("3) relu")
    
    # Leer la opción del usuario
    op = input("Your Option: ")

# Definir Entradas, pesos y bias fijos (como en exp2.py)
inputs = np.array([1.0, 0.5, -1.0])
weights = np.array([0.2, 0.5, 0.3])
bias = 0.4

# Calcula Suma ponderada (scalar)
weighted_sum = np.dot(inputs, weights) + bias

# Imprimir entradas, pesos y bias
print()
print("Entradas:", inputs)
print("Pesos:", weights)
print("Bias:", bias)
print("Suma ponderada:", weighted_sum)
print()

# Selección de la función de activación y cálculo de la salida
if op == '1':
    #calcula la funcion tanh en la suma ponderada
    y = np.tanh(weighted_sum)
    out = inputs.copy()
    np.tanh(inputs, out=out, where=True)
    
    lbl = "Tangente Hiperbolica"
    
    print("Resultado de Tangente Hiperbolica: ", out)
    print()
    print("Resultado Funcion de Activacion (tanh):", y)
elif op == '2':
    #calcula la funcion sigmoid en la suma ponderada
    y = 1 / (1 + np.exp(-weighted_sum))
    out = 1 / (1 + np.exp(-inputs))
    
    lbl = "Sigmoid"
    
    print("Resultado de Sigmoid: ", out)
    print() 
    print("Resultado Funcion de Activacion (sigmoid):", y)
else:
    #calcula la funcion relu en la suma ponderada
    y = max(0, weighted_sum)
    out = np.maximum(0, inputs)
    
    lbl = "ReLU"
    