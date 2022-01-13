from Pre_systems.pre_semi_system import *
from ternary_orbits import *
from Systems_of_Sheffer_Number_1_II import *
import time


t0 = time.time()

pre_sys = [[[0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 1, 0]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1, 1, 1, 1]]]


for i in range(len(clean_orbit)):
    for j in range(len(clean_orbit)):
        if i < j:
            if clean_orbit[i] not in sys_and_basis_II[j][1]:
                if clean_orbit[j] not in sys_and_basis_II[i][1]:
                    if pre_semi([], [], [clean_orbit[i], clean_orbit[j]]) not in pre_sys:
                        pre_sys.append(pre_semi([], [], [clean_orbit[i], clean_orbit[j]]))
                    print(i, j)
t1 = time.time()


for i in pre_sys:
    print(i)
print(len(pre_sys))
print(pre_sys)
print(t1-t0)
