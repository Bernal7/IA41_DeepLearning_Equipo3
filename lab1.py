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