#Ejercicios pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("personas.csv")
print("Datos originales", data)

#normalizar datos
max_edad = np.max(data["Edad"])
data["Edad_Normalizada"] = data["Edad"] / max_edad

print("Datos normalizados: ", data)

#Graficar
plt.plot(data["Nombre"], data["Edad"], label="Edad real", maker="o")
plt.plot(data["Nombre"], data["Edad_Normalizada"] * max_edad, label="edad normalizada * max", maker="x")
plt.title("Comparacion entre edad real y normalizada")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.legend()
plt.grid(True)
plt.show()