from Other_stuff.modules_gen_sys_ter import *
import time


pre_systems = [[[0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1]], [[0, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]], [[1, 1, 1, 1, 1, 1, 1, 1]]]
#
# t0 = time.time()


def ter_ter_closure(pre_system):
    for j in pre_system:
        for k in pre_system:
            for m in pre_system:
                for n in pre_system:
                    if len(pre_system) < 128:
                        if iteration_ter_ter(j, k, m, n) not in pre_system:
                            pre_system.append(iteration_ter_ter(j, k, m, n))
                    else:
                        pre_system = ter_val_col
                        break
    return sorted(pre_system)

# ter_closed = [ter_ter_closure(semi_sys[i]) for i in range(len(semi_sys))]
#
# systems = []
# for i in range(len(ter_closed)):
#     if ter_closed[i] not in systems:
#         systems.append((ter_closed[i]))



#
# print(len(ter_closed))
# print(len(systems))



# print(len(systems), systems)
#
#
# t1 = time.time()
# print(len(systems), systems)
# print(t1-t0)