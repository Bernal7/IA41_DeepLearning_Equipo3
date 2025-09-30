
#todo: 
#1) Investigar que es un "peso"
#2) Investigar que es un "bias"
#3) Implementar una neurona simple sin entrenar (solo pesos y bias elegidos a mano) que simule una compuerta lógica "NAND"
#4) Realizar un diagrama de flujo de la neurona simple implementada en "Draw.io" y subir la imagen a el reporte


#! Neurona simple sin entrenar
#? Solo pesos y bias elegidos a mano para simular un AND lógico

#* Datos de entrada (x1, x2)
entradas = [[0,0], [0,1], [1,0], [1,1]]

#*Pesos y bias (ajustados a mano)
w1, w2, b = 1, 1, -1.5

#!Función de activación (escalón)
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