from Pre_systems_and_Semi_systems.pre_sys_def import *
from Other_stuff.ternary_orbits import *
from sh_num_3_file import *
from Other_stuff.Systems_of_Sheffer_Number_1_II import *
import time


t0 = time.time()

sh_4 = []

for i in range(len(clean_orbit)):
    for j in range(len(clean_orbit)):
        for k in range(len(clean_orbit)):
            for m in range(len(clean_orbit)):
                if i < j:
                    if j < k:
                        if k < m:
                            if pre_sys([], [], [clean_orbit[i], clean_orbit[j], clean_orbit[k], clean_orbit[m]]) not in sheff_3:
                                print(pre_sys([], [], [clean_orbit[i], clean_orbit[j], clean_orbit[k], clean_orbit[m]]))
                                if pre_sys([], [], [clean_orbit[i], clean_orbit[j], clean_orbit[k], clean_orbit[m]]) not in sh_4:
                                    sh_4.append(pre_sys([], [], [clean_orbit[i], clean_orbit[j], clean_orbit[k], clean_orbit[m]]))
t1 = time.time()


print(sh_4)
print(len(sh_4))
print(t1-t0)
