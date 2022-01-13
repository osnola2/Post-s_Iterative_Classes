from iteration_unary_binary import *


def iteration_bin_bin(func_1, func_2, func_3):
    return [func_1[bin_t_v_num([func_2[i], func_3[i]])] for i in range(4)]






















# for i in range(len(bin_val_col)):
#     print(i, bin_val_col[i])
# print(bin_val_col[1], bin_val_col[13], bin_val_col[11])
# print([[bin_val_col[13][i], bin_val_col[11][i]] for i in range(4)])
# print([bin_t_v_num([bin_val_col[13][i], bin_val_col[11][i]]) for i in range(4)])
# print([bin_val_col[1][bin_t_v_num([bin_val_col[13][i], bin_val_col[11][i]])] for i in range(4)])
# 
# 
# for i in bin_val_col:
#     for j in bin_val_col:
#         for k in bin_val_col:
#             print(i, j, k, '_______', iteration_bin_bin(i, j, k))