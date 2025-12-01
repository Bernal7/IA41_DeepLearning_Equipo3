#libreria skfuzzy
import skfuzzy as fuzz
import numpy as np

#1 se define el rango del universo (temperatura de 0 a 30)
x_temp = np.arange(0, 31, 1)

#2 se define la funcion de pertenencia triangular (x, [iniciom centro, final])
mu_frio = fuzz.trimf(x_temp, [0, 0, 20])

#3 evaluamos la pertenencia de algunos valores
valores = [0, 5, 10, 15, 20]
