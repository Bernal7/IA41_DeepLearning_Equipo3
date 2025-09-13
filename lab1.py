# calificaciones conocidas
pepito_sherk = 5
pepito_jackass = 5

# Ramona calificaciones
Ramona_sherk = 1
Ramona_jackass = None

# Alvin calificaciones conocidas
Alvin_sherk = 4
Alvin_jackass = 2

# !Paso 1: calcular la similitud entre pepito (U) y Ramona (V).
numerador = pepito_sherk * Ramona_sherk
denominador = (pepito_sherk**2)**0.5 * (Ramona_sherk**2)**0.5
similitud1 = numerador / denominador

# !Paso 2: Calcular la similitud entre pepito (U) y Alvin (V)
numerador = pepito_sherk * Alvin_sherk
denominador = (pepito_sherk**2)**0.5 * (Alvin_sherk**2)**0.5
similitud2 = numerador / denominador

# !Paso 3: Calcular la prediccion
numerador = ((similitud1 * pepito_jackass) + (similitud2 * Alvin_jackass))
denominador = (similitud1 + similitud2)
prediccion = numerador / denominador

# !Resultados
print("Similitud Pepito-Ramona: ", round(similitud1, 2))
print("Similitud Pepito-Alvin: ", round(similitud2, 2))
print("Prediccion de Ramona para jackass: ", round(prediccion, 2))
