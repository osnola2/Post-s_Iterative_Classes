from pre_sys_def import *
from Other_stuff.ternary_orbits import *

import time


t0 = time.time()

pre_systems = []

for i in clean_orbit:
    if pre_sys([], [], [i]) not in pre_systems:
        pre_systems.append(pre_sys([], [], [i]))

t1 = time.time()


for i in pre_systems:
    print(i)
print(len(pre_systems))
print(pre_systems)
print(t1-t0)
