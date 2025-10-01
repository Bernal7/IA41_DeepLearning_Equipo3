#INVESTIGACIONES
#QUE ES UN PESO:
#Son valores numericos que determinan la importancia de cada entrada en una neurona, ayudana a ajustar la influencia que tiene cada variable de entrada de salida final

#QUE ES UN "BIAS"
#Es un valor adicional que suma al resultado de la combinacion lineal de entrada y pesos. Permite desplazar la funcion de activacion, ayudando a que la neruona modele funciones mas complejas

#NEURONA SIMPLE SIN ENTRENAR (PESOS ELEGIDOS A MANO) QUE SIMULE COMPUERTA LOGICA AND
#Datos de entrada (x1, x2) -> tabla de verdad NAND
entradas = [[0,0], [0,1], [1,0], [1,1]]

#Pesos y bias (ajustados para NAND)
w1, w2, b = 1, 1, -1.5

#Funcion de activacion
def step(x):
    """Funcion de activacion de escalon"""
    if x<=0:
        return 1
    else:
        return 0

print("Simulacion de una sola neurona (NAND Logico):\n")
for x in entradas:
    x1, x2 = x
    #Calculo de neuronas
    z = x1*w1 + x2*w2 + b
    salida = step(z)
    print(f"Entrada: {x} -> z={z:.1f}, salida={salida}")

#DIAGRAMA DE FLUJO DE LA NEURONA IMPLEMENTADA EN DRAW.IO