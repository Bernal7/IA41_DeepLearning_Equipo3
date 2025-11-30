import random
#Todo rear una solucion al azar (0--10)
def crear_individuo():
    return random.random(0, 10)


#! calcular el fitness de un individuo
def fitness(x):
    return x # entre mas grande mejor

#Todo proceso de seleccion
def seleccion(poblacion):
    a = random.choices(poblacion)
    b = random.choices(poblacion)
    return a if fitness(a) > fitness(b) else b

#!crossover entre los individuos
def cruzar(p1, p2):
    return (p1 + p2) // 2

#!Mutacion -- cambiar un individuo al azar
def mutar(x):
    if random.random() < 0.1: #probabilidad de mutacion
        return random.randit(0, 10)
    return x

#Todo algortimo genetico
def ga():
    poblacion = [crear_individuo for _ in range(5)]
    
