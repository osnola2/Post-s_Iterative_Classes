from iteration_ternary_binary import *


def generated_system_ter(base_un, base_bin, base_ter):
    for i in base_ter:
        if unary_reduct(i) not in base_un:
            base_un.append(unary_reduct(i))
    for i in base_ter:
        if first_colapse(i) not in base_bin:
            base_bin.append(first_colapse(i))
    for i in base_ter:
        if second_colapse(i) not in base_bin:
            base_bin.append(second_colapse(i))
    for i in base_ter:
        if third_colapse(i) not in base_bin:
            base_bin.append(third_colapse(i))
    print(base_bin)
    for i in base_un:
        for j in base_un:
            if iteration_un(i, j) not in base_un:
                base_un.append(iteration_un(i, j))
    if [0, 0, 1, 1] in base_bin:
        if [0, 0, 0, 0, 1, 1, 1, 1] not in base_ter:
            base_ter.append([0, 0, 0, 0, 1, 1, 1, 1])
    for i in base_bin:
        for j in base_un:
            if iteration_un_bin(j, i) not in base_bin:
                base_bin.append(iteration_un_bin(j, i))
    for i in base_bin:
        for j in base_un:
            if iteration_bin_un_1(i, j) not in base_bin:
                base_bin.append(iteration_bin_un_1(i, j))
    for i in base_bin:
        for j in base_un:
            if iteration_bin_un_2(i, j) not in base_bin:
                base_bin.append(iteration_bin_un_2(i, j))
    for i in base_bin:
        for j in base_bin:
            for k in base_bin:
                if iteration_bin_bin(i, j, k) not in base_bin:
                    base_bin.append(iteration_bin_bin(i, j, k))
    for i in base_bin:
        if perm(i) not  in base_bin:
            base_bin.append(perm(i))
    for i in base_bin:
        if unary_reduct(i) not in base_un:
            base_un.append(unary_reduct(i))
    print('base_bin', base_bin)
    for i in base_ter:
        for j in perm_ter:
            if j(i) not in base_ter:
                base_ter.append(j(i))
    print('base_ter')
    for i in base_ter:
        for j in base_ter:
            for k in base_bin:
                if iteration_bin_ter(k, i, j) not in base_ter:
                    base_ter.append(iteration_bin_ter(k, i, j))
    print(base_ter)

    if base_bin != bin_val_col:
        for i in base_ter:
            for j in base_bin:
                for k in base_bin:
                    for m in base_bin:
                        if iteration_ter_bin(i, j, k, m) not in base_bin:
                            base_bin.append(iteration_ter_bin(i, j, k, m))
    print('ter_bin', base_ter)
    for i in base_ter:
        for j in base_ter:
            for k in base_ter:
                for m in base_ter:
                    print(i, j, k, m, iteration_ter_ter(i, j, k, m))
                    if iteration_ter_ter(i, j, k, m) not in base_ter:
                        base_ter.append(iteration_ter_ter(i, j, k, m))
                        print('base_ter', base_ter)

    return sorted(base_ter), sorted(base_bin), sorted(base_un)



for i in range(len(ter_val_col)):
    print(i, ter_val_col[i])
print(generated_system_ter([], [[1, 0, 0, 0]], []))



#
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))

