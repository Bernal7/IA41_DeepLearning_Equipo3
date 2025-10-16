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
