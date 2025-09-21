import math

usuarios = { 
    "usuario1": {"La isla": 4, "Interestellar": 5, "Pokemon": None},
    "usuario2": {"La isla": 2, "Interestellar": None, "Pokemon": 5},
    "usuario3": {"La isla": 3, "Interestellar": 5, "Pokemon": 4},
}

#funcion para calcular la similitud de usuario1 y usuario2, SIMILITUD ESPERADA ALREDEDOR DE 0.23
def similitud (u1, u2):
    suma = 0
    for item in usuarios[u1]:
        if usuarios[u1][item] is not None and usuarios[u2][item] is not None:
            suma += math.pow(usuarios[u1][item] - usuarios[u2][item],2)
        return 1 / (1 + math.sqrt(suma))
    
def predecir(usuario_objetivo, item_objetivo):
    num, den = 0, 0
    for otro in usuarios:
        if otro != usuario_objetivo and usuarios[otro][item_objetivo] is not None:
            sim = similitud(usuario_objetivo, otro)
            num += sim * usuarios[otro][item_objetivo]
            den += abs(sim)
    return num / den if den != 0 else 0

#PREDICCION ESPERADA ALREDEDOR DE 4.03 Y 4.25 RESPECTIVAMENTE
print("Similitud usuario1 - usuario2:", similitud("usuario1", "usuario2")) #SIM ESPERADA DE 0.23
print("Similitud usuario1 - usuario3:", similitud("usuario1", "usuario3")) #SIM ESPERADA DE 7.07
print("Similitud usuario2 - usuario3:", similitud("usuario2", "usuario3")) #SIM ESPERADA DE 0.68

print("\nPredicciones:")
print("usuario1 en Pokemon:", predecir("usuario1", "Pokemon")) #PRED ESPERADA DE 4.03
print("usuario2 en Interstellar:", predecir("usuario2", "Interestellar")) #PRED ESPERADA DE 4.25