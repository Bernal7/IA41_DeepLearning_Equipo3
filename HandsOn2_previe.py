import math #libreria para operaciones matematicas avanzadas y las que se van a usar

#declaracion en array de las calificaciones de la tabla de usuarios
usuarios = {
    "usuario1": {"Pokermon": 3.5, "Naruto": 5, "Demon Slayer": None},
    "usuario2": {"Pokermon": 2.5, "Naruto": None, "Demon Slayer": 3.5},
    "usuario3": {"Pokermon": None, "Naruto": 4.5, "Demon Slayer": 4.5},
    "usuario4": {"Pokermon": 2.5, "Naruto": 3.5, "Demon Slayer": 4.5},
}
#resumen
#usuarios  = tabla de calificaciones
#item = cada serie/película que se compara
#similitud(u1, u2) = qué tan parecidos son dos usuarios según sus calificaciones
#predecir(usuario, item) = cuánto se espera que le guste a un usuario un ítem que no calificó.

#funcion de similitud entre los primeros dos usuarios, SALIDA ESPERADA ALREDEDOR DE 0.33 
# --- Función de similitud euclidiana inversa ---
def similitud(u1, u2):
    suma = 0 #todas las diferencias de cudrados en la operacion
    for item in usuarios[u1]: #item es la representacion de cada serie
        if usuarios[u1][item] is not None and usuarios[u2][item] is not None: #Se asegura de comparar solo los ítems donde ambos usuarios dieron calificación.
            suma += math.pow(usuarios[u1][item] - usuarios[u2][item], 2) #calcula la diferencia de calificaciones al cuadrado
    return 1 / (1 + math.sqrt(suma)) #formula para convertir la distancia en similitud mas cercana a 1

# --- Predicción de un ítem faltante ---
def predecir(usuario_objetivo, item_objetivo):
    num, den = 0, 0 #declaracion numerador y denominador
    for otro in usuarios: #algoritmo recorre los demas usuarios
        if otro != usuario_objetivo and usuarios[otro][item_objetivo] is not None: #IMPORTANTE: Solo se considera a los que si hayan calificado
            sim = similitud(usuario_objetivo, otro) #que tan parecidos es el Uactual al otro
            num += sim * usuarios[otro][item_objetivo] #Mult. del otro usuario por la similitud
            den += abs(sim)
    return num / den if den != 0 else 0 #promedio de calificaciones, prediccion

# --- Ejemplo --- SALIDA ESPERADA ALREDEDOR O SIMILARES DE 4.32
print("Similitud usuario1 - usuario2:", similitud("usuario1", "usuario2"))
print("Predicción usuario1 en Demon Slayer:", predecir("usuario1", "Demon Slayer"))