from Basic_definitions_and_iterations.iteration_unary import *
from Basic_definitions_and_iterations.iteration_ternary_binary import *


def binary_frag(base_un, base_bin, base_ter):
    for i in base_ter:
        for j in colapses:
            if j(i) not in base_bin:
                base_bin.append(j(i))
    return base_un, base_bin, base_ter


def binary_sys(base_un, base_bin, base_ter):
    for i in base_bin:
        if unary_reduct(i) not in base_un:
            base_un.append(unary_reduct(i))
    if base_un != un_val_col:
        for i in base_un:
            for j in base_un:
                if iteration_un(i, j) not in base_un:
                    base_un.append(iteration_un(i, j))
    if base_bin != bin_val_col:
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
            if perm(i) not in base_bin:
                base_bin.append(perm(i))
        for i in base_bin:
            if unary_reduct(i) not in base_un:
                base_un.append(unary_reduct(i))
    return base_un, base_bin, base_ter


def un_close_ter(base_un, base_bin, base_ter):
    for i in base_ter:
        for j in base_un:
            if iteration_un_ter(j, i) not in base_ter:
                base_ter.append(iteration_un_ter(j, i))
    return base_un, base_bin, base_ter


def bin_close_ter(base_un, base_bin, base_ter):
    for i in base_ter:
        for j in base_ter:
            for k in base_bin:
                if iteration_bin_ter(k, i, j) not in base_ter:
                    base_ter.append(iteration_bin_ter(k, i, j))
    return base_un, base_bin, base_ter


def ter_close_bin(base_un, base_bin, base_ter):
    if base_bin != bin_val_col:
        for i in base_ter:
            for j in base_bin:
                for k in base_bin:
                    for m in base_bin:
                        if iteration_ter_bin(i, j, k, m) not in base_bin:
                            base_bin.append(iteration_ter_bin(i, j, k, m))
    return base_un, base_bin, base_ter


def proj_closure_ter(base_un, base_bin, base_ter):
    if [0, 0, 1, 1] in base_bin:
        if [0, 0, 0, 0, 1, 1, 1, 1] not in base_ter:
            base_ter.append([0, 0, 0, 0, 1, 1, 1, 1])
    return base_un, base_bin, base_ter


def perm_closure_ter(base_un, base_bin, base_ter):
    for i in base_ter:
        for j in perm_ter:
            if j(i) not in base_ter:
                base_ter.append(j(i))
    return base_un, base_bin, base_ter

# print(proj_closure_ter([[]], [[]], [[0, 0, 0, 0, 1, 1, 1, 1]]))