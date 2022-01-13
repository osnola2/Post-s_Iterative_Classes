from basic_definitions import *

iteration_unit = [[i, j, [i[j[0]], i[j[1]]]] for i in un_val_col for j in un_val_col]

def iteration_un(func1, func2):
    return [func1[func2[0]], func1[func2[1]]]

print(iteration_unit)

for i in un_val_col:
    for j in un_val_col:
        print(i, j, iteration_un(i, j))