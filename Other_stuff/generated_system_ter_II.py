from Basic_definitions_and_iterations.iteration_ternary_binary import *
from modules_gen_sys_ter import *

def generated_system_ter(base_un, base_bin, base_ter):
    print('base_ter', base_ter)
    binary_frag(base_un, base_bin, base_ter)
    print('binary_frag', base_bin)
    binary_sys(base_un, base_bin, base_ter)
    print('binary_sys', len(base_bin), base_bin)
    if len(base_bin) < 16:
        print('base_ter', len(base_ter), base_ter)
        proj_closure_ter(base_un, base_bin, base_ter)
        perm_closure_ter(base_un, base_bin, base_ter)
        print('base_ter_proj_perm', len(base_ter), base_ter)
        un_close_ter(base_un, base_bin, base_ter)
        print('base_ter_un_close', len(base_ter), base_ter)
        bin_close_ter(base_un, base_bin, base_ter)
        print('bin_close_ter', len(base_ter), base_ter)
        ter_close_bin(base_un, base_bin, base_ter)
        print('ter_close_bin', len(base_bin), base_bin)
        # if len(base_bin) < 16:
        #     bin_close_ter(base_un, base_bin, base_ter)
        #     print('bin_close_ter', len(base_ter), base_ter)
        #     ter_close_bin(base_un, base_bin, base_ter)
        #     print('ter_close_bin', len(base_bin), base_bin)
        #     binary_frag(base_un, base_bin, base_ter)
        #     print('base_bin', len(base_bin), base_bin)
        # else:
        #     base_ter = ter_val_col
    else:
        base_ter = ter_val_col

    if len(base_ter) < 128:
        for i in base_ter:
            for j in base_ter:
                for k in base_ter:
                    for m in base_ter:
                        if iteration_ter_ter(i, j, k, m) not in base_ter:
                            base_ter.append(iteration_ter_ter(i, j, k, m))
                            print('new_base_ter', base_ter, len(base_ter))

    return sorted(base_ter)



# for i in range(len(ter_val_col)):
#     print(i, ter_val_col[i])
# print(generated_system_ter([], [], [[1, 0, 0, 1, 0, 0, 0, 0]]))



#
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))

