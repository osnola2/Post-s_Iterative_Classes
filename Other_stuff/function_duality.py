from Post_Iterative_Systems import *
from ter_ter_closure import *

def dual(sequence):
    return [1-sequence[7], 1-sequence[6], 1-sequence[5], 1-sequence[4],
            1-sequence[3], 1-sequence[2], 1-sequence[1], 1-sequence[0]]

# for i in systems[21]:
#   print(i, dual(i))

a = []

for i in systems:
    for j in systems:
        if sorted(list(map(lambda x : dual(x), i))) == sorted(j):
            if i != j:
                if [i, j] not in a:
                    a.append([i, j])
print(len(a))

b = []

for i in systems:
    for j in systems:
        if sorted(list(map(lambda x: dual(x), i))) == sorted(j):
            if i == j:
                if [i, j] not in b:
                    b.append([i, j])
print(len(b))
#

# print('___________________________')
#
# a = []
#
# for i in systems:
#     if sorted(list(map(lambda x : dual(x), i))) == sorted(i):
#         a.append(i)
# print(len(a))
#
# b = []
#
# for i in a:
#     if [0, 0, 0, 0, 1, 1, 1, 1] in i:
#         b.append(i)
# print(len(b))
# for i in b:
#     print(i)
#
# print('__________________________')
#
# c = []
#
# for i in systems:
#     if all(dual(j) == j for j in i):
#         if sorted(i) not in c:
#             c.append(sorted(i))
# print(len(c))
#
#
# for i in c:
#     for j in i:
#         if j != [0, 0, 0, 0, 1, 1, 1, 1]:
#             if j != [0, 0, 1, 1, 0, 0, 1, 1]:
#                 if j != [0, 1, 0, 1, 0, 1, 0, 1]:
#                     print(j)
#     print('____________')
#
#
#
# for i in c:
#     if sorted(ter_ter_closure(i)) != sorted(i):
#         print(i)
#         print(ter_ter_closure(i))
#         print('))')

