from generated_system_ter_IV import *
from ternary_orbits import *
import time

t0 = time.time()

systems = []

for i in range(len(clean_orbit)):
    if generated_system_ter([], [], [clean_orbit[i]]) not in systems:
        systems.append(generated_system_ter([], [], [clean_orbit[i]]))
    # print(systems)


for i in systems:
    print(i)
print(len(systems))
print("_______________")
print(systems)

t1 = time.time()
print(t1-t0)