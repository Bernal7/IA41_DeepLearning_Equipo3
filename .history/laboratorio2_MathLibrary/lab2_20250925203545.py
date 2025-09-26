
# * importar libreria Math para calcular exponentes y racices cuadradas
import math
# * importar libreria Math para calcular exponentes y racices cuadradas





# ? Definir calificacion de los usuarios segun la pelicula

usuario1_pokemon = 3.5
usuario1_naruto = 5
usuario1_demon = None

usuario2_pokemon = 2.5
usuario2_naruto = None
usuario2_demon = 3.5

usuario3_pokemon = None
usuario3_naruto = 4.5
usuario3_demon = 4.5

usuario4_pokemon = 2.5
usuario4_naruto = 3.5
usuario4_demon = 4.5

# ? Definir calificacion de los usuarios segun la pelicula





# TODO Calcular Similitud #1 para usuario 1 y usuario 2

numerador = usuario1_pokemon * usuario2_pokemon

denominador = math.sqrt(math.pow(usuario1_pokemon, 2) * math.pow(usuario2_pokemon, 2))

sim1 = numerador / denominador

# TODO Calcular Similitud #1 para usuario 1 y usuario 2



# TODO Calcular Similitud #2 para usuario 1 y usuario 3

numerador = usuario1_naruto * usuario3_naruto

denominador = math.sqrt(math.pow(usuario1_naruto, 2) * math.pow(usuario3_naruto, 2))

sim2 = numerador / denominador

# TODO Calcular Similitud #2 para usuario 1 y usuario 3



# TODO Calcular Similitud #3 para usuario 1 y usuario 4

numerador = (usuario1_pokemon * usuario4_pokemon) + (usuario1_naruto * usuario4_naruto)

denominador = math.sqrt((math.pow(usuario1_pokemon, 2) + math.pow(usuario1_naruto, 2)) * (math.pow(usuario4_pokemon, 2) + math.pow(usuario4_naruto, 2)))

sim3 = numerador / denominador

# TODO Calcular Similitud #3 para usuario 1 y usuario 4



# TODO Calcular Similitud #4 para usuario 2 y usuario 3

numerador = usuario2_demon * usuario3_demon

denominador = math.sqrt(math.pow(usuario2_demon, 2) * math.pow(usuario3_demon, 2))

sim4 = numerador / denominador

# TODO Calcular Similitud #4 para usuario 2 y usuario 3



# TODO Calcular Similitud #5 para usuario 2 y usuario 4

numerador = (usuario2_pokemon * usuario4_pokemon) + (usuario2_demon * usuario4_demon)

denominador = math.sqrt((math.pow(usuario2_pokemon, 2) + math.pow(usuario2_demon, 2)) * (math.pow(usuario4_pokemon, 2) + math.pow(usuario4_demon, 2)))

sim5 = numerador / denominador

# TODO Calcular Similitud #5 para usuario 2 y usuario 4



# TODO Calcular Similitud #6 para usuario 3 y usuario 4

numerador = (usuario3_naruto * usuario4_naruto) + (usuario3_demon * usuario4_demon)

denominador = math.sqrt((math.pow(usuario3_naruto, 2) + math.pow(usuario3_demon, 2)) * (math.pow(usuario4_naruto, 2) + math.pow(usuario4_demon, 2)))

sim6 = numerador / denominador

# TODO Calcular Similitud #6 para usuario 3 y usuario 4





# ! Calcular Prediccion para Usuario 1 Demon Slayer

numerador = (sim1 * usuario2_demon) + (sim2 * usuario3_demon) + (sim3 * usuario4_demon)

denominador = sim1 + sim2 + sim3

pred1 = numerador / denominador

# ! Calcular Prediccion para Usuario 1 Demon Slayer



# ! Calcular Prediccion para Usuario 2 Naruto

numerador = (sim1 * usuario1_naruto) + (sim4 * usuario3_naruto) + (sim5 * usuario4_naruto)
denominador = sim1 + sim4 + sim5
pred2 = numerador / denominador

# ! Calcular Prediccion para Usuario 2 Naruto



# ! Calcular Prediccion para Usuario 3 Pokemon

numerador = (sim2 * usuario1_pokemon) + (sim4 * usuario2_pokemon) + (sim6 * usuario4_pokemon)
denominador = sim2 + sim4 + sim6
pred3 = numerador / denominador

# ! Calcular Prediccion para Usuario 3 Pokemon





# * Imprimir Resultados de el Calculo de Similitudes y Calculo de  Predicciones 

print("Similitud #1 entre: usuario #1 vs usuario #2 = ", sim1) # ? Impresion de Resultado de la Primera Similitud
print("Similitud #2 entre: usuario #1 vs usuario #3 = ", sim2) # ? Impresion de Resultado de la Segunda Similitud
print("Similitud #3 entre: usuario #1 vs usuario #4 = ", sim3) # ? Impresion de Resultado de la Tercera Similitud
print("Similitud #4 entre: usuario #2 vs usuario #3 = ", sim4) # ? Impresion de Resultado de la Cuarta Similitud
print("Similitud #5 entre: usuario #2 vs usuario #4 = ", sim5) # ? Impresion de Resultado de la Quinta Similitud
print("Similitud #6 entre: usuario #3 vs usuario #4 = ", sim6) # ? Impresion de Resultado de la Sexta Similitud

print()

print("Prediccion para: Usuario #1 - Demon Slayer = ", pred1) # ? Impresion del Resultado de la Primera Prediccion
print("Prediccion para: Usuario #2 - Naruto = ", pred2) # ? Impresion del Resultado de la Segunda Prediccion
print("Prediccion para: Usuario #3 - Pokemon = ", pred3) # ? Impresion del Resultado de la Tercera Prediccion

# * Imprimir Resultados de el Calculo de Similitudes y Calculo de  Predicciones