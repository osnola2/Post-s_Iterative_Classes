from iteration_unary import *


def unary_reduct(func):
    return [func[0], func[-1]]

def perm(bin_func):
    return [bin_func[0], bin_func[2], bin_func[1], bin_func[3]]
    

def iteration_un_bin(func1, func2):
    return [func1[func2[0]], func1[func2[1]], func1[func2[2]], func1[func2[3]]]


def bin_t_v_num(bin_t_v):
    if bin_t_v == [0, 0]:
        return 0
    if bin_t_v == [0, 1]:
        return 1
    if bin_t_v == [1, 0]:
        return 2
    if bin_t_v == [1, 1]:
        return 3


def iteration_bin_un_1(func2, func1):
        return (list(map(lambda x : func2[bin_t_v_num([func1[x[0]], x[1]])], bin_truth_val)))


def iteration_bin_un_2(func2, func1):
    return (list(map(lambda x: func2[bin_t_v_num([x[0], func1[x[1]]])], bin_truth_val)))




# print(iteration_bin_un_1(bin_val_col[13], un_val_col[2]))
# print(iteration_bin_un_2(bin_val_col[13], un_val_col[2]))
# 
# for i in bin_val_col:
#     print(i, iteration_bin_un_1(i, [1, 0]), iteration_bin_un_2(i, [1, 0]))


# for i in bin_truth_val:
#     print(i, [un_val_col[3][i[0]], i[1]], [k for k in range(4) if bin_truth_val[k] == [un_val_col[3][i[0]], i[1]]])

# for i in bin_truth_val:
#     for j in [un_val_col[2]]:
#         print(i, j, [j[i[0]], i[1]], bin_t_v_num([j[i[0]], i[1]]),bin_val_col[13], bin_val_col[13][bin_t_v_num([j[i[0]], i[1]])])