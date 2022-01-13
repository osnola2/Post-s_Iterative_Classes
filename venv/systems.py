from generated_system import *

systems = []
for i in bin_val_col:
    for j in bin_val_col:
        for k in bin_val_col:
            if i != j:
                if i != k:
                    if j != k:
                        if generated_system([], [i, j, k]) not in systems:
                            systems.append(generated_system([], [i, j, k]))

for i in systems:
    print(i)
print(len(systems))