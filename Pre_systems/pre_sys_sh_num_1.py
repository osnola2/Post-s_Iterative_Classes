from Pre_systems.pre_semi_system import *
from ternary_orbits import *
import time


t0 = time.time()

pre_sys = []

for i in clean_orbit:
    if pre_semi([], [], [i]) not in pre_sys:
        pre_sys.append(pre_semi([], [], [i]))

t1 = time.time()


for i in pre_sys:
    print(i)
print(len(pre_sys))
print(pre_sys)
print(t1-t0)
