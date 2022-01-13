from Semi_systems.semi_system_ter import *
from ternary_orbits import *
from Systems_of_Sheffer_Number_1_II import *
import time




semi_sys = []

t0 = time.time()

for i in range(len(clean_orbit)):
    if semi_system_ter([], [], [clean_orbit[i]]) not in semi_sys:
        semi_sys.append(semi_system_ter([], [], [clean_orbit[i]]))
    print(i)

t1 = time.time()
print(semi_sys)
print(len(semi_sys))
print(t1-t0)
