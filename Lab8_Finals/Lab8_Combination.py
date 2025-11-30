#Combinacion pandas y skfuzzy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

#1 cargar los datos al pandas, crear un dataframe como si fuera un archivo CSV
data = pd.DataFrame({
    "Nombre: " ["Ana", "Luis", "Sofia", "Pedro", "Maria"],
    "Edad: " [12, 25, 37, 50, 70]
})

print("Datos originales:\n", data)

#2 normalizar las edades
max_edad = np.max(data["Edad"])
data["Edad_Normalizada"] = data["Edad"] / max_edad

print("\nDatos con edad normalizada:\n", data)

#3 crear un sistema difuso para clasificar las edades (uso de skfuzzy)
#Universo de edades de 0 a 80
x_edad = np.arange(0, 81, 1)

#Funciones difusas triangulares
mu_joven = fuzz.trimf(x_edad, [0, 0, 30])
mu_adulto = fuzz.trimf(x_edad, [20, 40, 60])
mu_mayor = fuzz.trimf(x_edad, [50, 80, 80])

#Calcular pertenencia difusa de cada edad del dataframe
pertenencia_joven = []
pertenencia_adulto = []
pertenencia_mayor = []

for e in data["Edad"]:
    pertenencia_joven.append(fuzz.interp_membership(x_edad, mu_joven, e))
pertenencia_adulto.append(fuzz.interp_membership(x_edad, mu_adulto, e))
    pertenencia_mayor.append(fuzz.interp_membership(x_edad, mu_mayor, e))

data["mu_joven"] = pertenencia_joven
data["mu_adulto"] = pertenencia_adulto
data["mu_mayor"] = pertenencia_mayor

print("\nPertenencias difusas calculadas:\n", data)

#4 graficacion
plt.figure(figsize=(10,5))
