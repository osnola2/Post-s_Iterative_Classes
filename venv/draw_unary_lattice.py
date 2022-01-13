cover_rel = [[[], [0]] ,
[[], [1]] ,
[[], [3]] ,
[[0], [0, 1]] ,
[[0], [0, 3]] ,
[[1], [1, 2]] ,
[[1], [0, 1]] ,
[[1], [1, 3]] ,
[[1, 2], [0, 1, 2, 3]] ,
[[3], [0, 3]] ,
[[3], [1, 3]] ,
[[0, 1], [0, 1, 3]] ,
[[0, 3], [0, 1, 3]] ,
[[1, 3], [0, 1, 3]] ,
[[0, 1, 3], [0, 1, 2, 3]]]

sys_by_lenght = [[[]], [[0], [1], [3]], [[1, 2], [0, 1], [0, 3], [1, 3]], [[0, 1, 3]], [[0, 1, 2, 3]]]

canvas = (700, 900)
place_bot = (canvas[0]/2, canvas[1]-50)
step = 50


pos_nodes = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
pos_nodes_aux = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(len(sys_by_lenght)):
    for j in range(len(sys_by_lenght[i])):
        start_point = (canvas[0]/(len(sys_by_lenght[i])+1), canvas[1]-40*i)
        step_lat = canvas[0]/(len(sys_by_lenght[i])+1)
        pos_nodes[i].append((start_point[0]+step_lat*j, start_point[1]))
        pos_nodes_aux[i].append(sys_by_lenght[i][j])


print('strokeWeight(8)')
print('stroke(0)')
for i in pos_nodes:
    for j in i:
        print('point', j)

# for i in range(len(pos_nodes)):
#     print(pos_nodes[i], pos_nodes_aux[i])


print('strokeWeight(0.5)')
for i in range(len(pos_nodes_aux)):
    for j in range(len(pos_nodes_aux)):
        for i1 in range(len(pos_nodes_aux[i])):
            for j1 in range(len(pos_nodes_aux[j])):
                if [pos_nodes_aux[i][i1],pos_nodes_aux[j][j1]] in cover_rel:
                    print('line(', pos_nodes[i][i1][0],',', pos_nodes[i][i1][1], ',', pos_nodes[j][j1][0], ',', pos_nodes[j][j1][1], ')')

# a = []
# b = []
# for i in one_el_cover:
#     if i[0] not in a:
#         a.append(i[0])
#     if i[1] not in b:
#         b.append(i[1])
# print(a)
# print(len(a))
# print(b)
# print(len(b))