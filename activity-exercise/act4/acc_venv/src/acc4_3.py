import numpy as np
import time

lista = (range(1_000_000))
t1 = time.time()

lista = [x * 2 for x in lista]
t2 = time.time()

print(f"tiempo con listas : {t2 - t1}")

array = np.arange(1_000_000)

t1 = time.time()

arra = array * 2

t2 = time.time()

print(f"tiempo con NumPy : {t2 - t1}")