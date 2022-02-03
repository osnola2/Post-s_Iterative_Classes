from Basic_definitions_and_iterations.iteration_ternary_binary import *
from Other_stuff.modules_gen_sys_ter import *


def pre_sys(base_un, base_bin, base_ter):
    binary_frag(base_un, base_bin, base_ter)
    binary_sys(base_un, base_bin, base_ter)
    if len(base_bin) < 16:
        proj_closure_ter(base_un, base_bin, base_ter)
        perm_closure_ter(base_un, base_bin, base_ter)
        un_close_ter(base_un, base_bin, base_ter)
        bin_close_ter(base_un, base_bin, base_ter)
        ter_close_bin(base_un, base_bin, base_ter)
        binary_frag(base_un, base_bin, base_ter)
    else:
        base_ter = ter_val_col
    return sorted(base_ter)



# for i in range(len(ter_val_col)):
#     print(i, ter_val_col[i])
# print(generated_system_ter([], [], [[1, 0, 0, 1, 0, 0, 0, 0]]))





#
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))

