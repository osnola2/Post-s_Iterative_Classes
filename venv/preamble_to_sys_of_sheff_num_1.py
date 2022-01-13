from generated_system_ter_III import *
from ternary_orbits import *
import time

t0 = time.time()

systems = []

for i in range(5):
    systems.append([i, generated_system_ter([], [], [clean_orbit[i]])])
    # print(systems)


for i in systems:
    print(i)
print(len(systems))
print("_______________")
print(systems)

t1 = time.time()
print(t1-t0)