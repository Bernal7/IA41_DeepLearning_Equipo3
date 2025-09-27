
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