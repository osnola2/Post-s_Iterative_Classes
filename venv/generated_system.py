from iteration_binary_binary import *


def generated_system(base_un, base):
    for i in base:
        if unary_reduct(i) not in base_un:
            base_un.append(unary_reduct(i))
    for i in base_un:
        for j in base_un:
            if iteration_un(i, j) not in base_un:
                base_un.append(iteration_un(i, j))
    for i in base:
        for j in base_un:
            if iteration_un_bin(j, i) not in base:
                base.append(iteration_un_bin(j, i))
    for i in base:
        for j in base_un:
            if iteration_bin_un_1(i, j) not in base:
                base.append(iteration_bin_un_1(i, j))
    for i in base:
        for j in base_un:
            if iteration_bin_un_2(i, j) not in base:
                base.append(iteration_bin_un_2(i, j))
    for i in base:
        for j in base:
            for k in base:
                if iteration_bin_bin(i, j, k) not in base:
                    base.append(iteration_bin_bin(i, j, k))
    for i in base:
        if perm(i) not  in base:
            base.append(perm(i))
    for i in base:
        if unary_reduct(i) not in base_un:
            base_un.append(unary_reduct(i))
    return sorted(base)


# for i in bin_val_col:
#     for j in bin_val_col:
#         print(i, j, generated_system([], [i, j]))



#
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[1]))
# print(sorted(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))
# print(len(generated_system([[1, 0]], [[1, 1, 1, 1]])[0]))

