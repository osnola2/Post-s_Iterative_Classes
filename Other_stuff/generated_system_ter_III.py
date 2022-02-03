from Basic_definitions_and_iterations.iteration_ternary_binary import *
from modules_gen_sys_ter import *

def generated_system_ter(base_un, base_bin, base_ter):
    binary_frag(base_un, base_bin, base_ter)
    binary_sys(base_un, base_bin, base_ter)
    if len(base_bin) < 16:
        proj_closure_ter(base_un, base_bin, base_ter)
        perm_closure_ter(base_un, base_bin, base_ter)
        un_close_ter(base_un, base_bin, base_ter)
        bin_close_ter(base_un, base_bin, base_ter)
        ter_close_bin(base_un, base_bin, base_ter)
        if len(base_bin) < 16:
            if len(base_ter) < 128:
                bin_close_ter(base_un, base_bin, base_ter)
                ter_close_bin(base_un, base_bin, base_ter)
                binary_frag(base_un, base_bin, base_ter)
    if len(base_ter) < 128:
        for i in base_ter:
            for j in base_ter:
                for k in base_ter:
                    for m in base_ter:
                        if iteration_ter_ter(i, j, k, m) not in base_ter:
                            base_ter.append(iteration_ter_ter(i, j, k, m))
    else:
        return base_ter



    return sorted(base_ter)




#
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))

