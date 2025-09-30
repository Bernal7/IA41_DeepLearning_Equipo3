entradas = [[0,0], [0,1], [1,0], [1,1]]

w1, w2, b = 1, 1, -1.5

def step(x):
    """Función de activación escalón"""
    if x >= 0:
        return 1
    else:
        return 0

print("Simulación de una sola neurona (AND lógico):\n")
for x in entradas:
    x1, x2 = x
    # cálculo de la neurona: z = x1*w1 + x2*w2 + b
    z = x1*w1 + x2*w2 + b
    salida = step(z)
    print(f"Entrada: {x} -> z={z:.1f}, salida={salida}")