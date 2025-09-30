import random
choice = random
import sys

print(f"random es choice?{random is choice}")

## verificamos carga el modulo
print(f"random en sys.modules: {'random' in sys.modules}")

print(f"ID Random: {id(random)}")
print(f"ID Random: {id(choice)}")
