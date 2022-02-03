from Basic_definitions_and_iterations.iteration_binary_binary import *


def first_colapse(ternary_function):
    return[ternary_function[0], ternary_function[1], ternary_function[-2], ternary_function[-1]]


def second_colapse(ternary_function):
    return [ternary_function[0], ternary_function[2], ternary_function[5], ternary_function[7]]


def third_colapse(ternary_function):
    return [ternary_function[0], ternary_function[3], ternary_function[4], ternary_function[7]]

colapses = [first_colapse, second_colapse, third_colapse]

def ter_t_v_num(sequence):
    if sequence == [0, 0, 0]:
        return 0
    if sequence == [0, 0, 1]:
        return 1
    if sequence == [0, 1, 0]:
        return 2
    if sequence == [0, 1, 1]:
        return 3
    if sequence == [1, 0, 0]:
        return 4
    if sequence == [1, 0, 1]:
        return 5
    if sequence == [1, 1, 0]:
        return 6
    if sequence == [1, 1, 1]:
        return 7


def iteration_ter_bin(ter_func, bin_func_1, bin_func_2, bin_func_3):
    return [ter_func[ter_t_v_num([bin_func_1[i], bin_func_2[i], bin_func_3[i]])] for i in range(4)]


def iteration_bin_ter(bin_func, ter_func_1, ter_func_2):
    return [bin_func[bin_t_v_num([ter_func_1[i], ter_func_2[i]])] for i in range(8)]


def iteration_ter_ter(ter_func1, ter_func_2, ter_func_3, ter_func_4):
    return [ter_func1[ter_t_v_num([ter_func_2[i], ter_func_3[i], ter_func_4[i]])] for i in range(8)]



def not_p_component(ter_func):
     return ter_func[:4]


def p_component(ter_func):
    return  ter_func[4:]

def perm_pqr(ter_fun):
    return list(map(lambda x : ter_fun[ter_t_v_num([x[0], x[1], x[2]])], ter_truth_val))



def perm_prq(ter_fun):
    return list(map(lambda x : ter_fun[ter_t_v_num([x[0], x[2], x[1]])], ter_truth_val))


def perm_qpr(ter_fun):
    return list(map(lambda x : ter_fun[ter_t_v_num([x[1], x[0], x[2]])], ter_truth_val))


def perm_qrp(ter_fun):
    return list(map(lambda x : ter_fun[ter_t_v_num([x[1], x[2], x[0]])], ter_truth_val))


def perm_rpq(ter_fun):
    return list(map(lambda x : ter_fun[ter_t_v_num([x[2], x[0], x[1]])], ter_truth_val))


def perm_rqp(ter_fun):
    return list(map(lambda x : ter_fun[ter_t_v_num([x[2], x[1], x[0]])], ter_truth_val))


perm_ter = [perm_pqr, perm_prq, perm_qpr, perm_qrp, perm_rpq, perm_rqp]


def iteration_un_ter(un_fun, ter_fun):
    return [un_fun[ter_fun[i]] for i in range(8)]


# print(iteration_un_ter([1, 0], [1, 1, 1, 1, 1, 0, 1, 1]))

# for i in range(len(ter_val_col)):
#     print(i, ter_val_col[i], not_p_component(ter_val_col[i]), p_component(ter_val_col[i]))

# print(iteration_ter_bin([0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 1]))
# for i in ter_truth_val:
#     print(i, ter_t_v_num(i), [i[1], i[0], i[2]], ter_t_v_num([i[1], i[0], i[2]]))
#
# print('__________________________________')
# for i in ter_truth_val:
#     print(i, ter_t_v_num(i), [i[2], i[1], i[0]], ter_t_v_num([i[2], i[1], i[0]]))
#
# print('__________________________________')
# for i in ter_truth_val:
#     print(i, ter_t_v_num(i), [i[2], i[0], i[1]], ter_t_v_num([i[2], i[0], i[1]]))
# print('__________________________________')
# for i in ter_truth_val:
#     print(i, ter_t_v_num(i), [i[2], i[1], i[0]], ter_t_v_num([i[2], i[1], i[0]]))
# print('__________________________________')
# for i in ter_truth_val:
#     print(i, ter_t_v_num(i), [i[2], i[1], i[0]], ter_t_v_num([i[2], i[1], i[0]]))
# print('__________________________________')
# for i in ter_truth_val:
#     print(i, ter_t_v_num(i), [i[1], i[2], i[0]], ter_t_v_num([i[2], i[1], i[0]]))
#
#
# print(perm_pq([0, 1, 0, 0, 1, 1, 0, 1]))
#
# orbits = []
#
# for i in ter_val_col:
#     orbit = [i]
#     for j in perm_ter:
#         if j(i) not in orbit:
#             orbit.append(j(i))
#     if sorted(orbit) not in orbits:
#         orbits.append(sorted(orbit))
#         print(i, sorted(orbit))
# print('________________________________________________________________________________________')
# for i in orbits:
#     print(i)
# print(len(orbits))
# print(orbits)
#
# print(iteration_bin_ter([0, 1, 1, 1], [0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1, 1]))
# print(iteration_ter_ter([0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]))