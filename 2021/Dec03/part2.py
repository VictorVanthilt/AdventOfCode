import numpy as np
file = [i.rstrip() for i in open('input.txt', 'r').readlines()]
file1, file2 = [np.array([[int(i) for i in j] for j in file]) for _ in range(2)]

def most_common(data):
    return int(sum(data) >= data.size/2)

for k in range(12):
    if file1[file1[:,k] == most_common(file1[:,k])].size > 1:
        file1 = file1[file1[:,k] == most_common(file1[:,k])]
    if file2[file2[:,k] == int(not most_common(file2[:,k]))].size > 1:
        file2 = file2[file2[:,k] == int(not most_common(file2[:,k]))]

print(int(''.join([str(i) for i in file1[0]]), 2) * int(''.join([str(i) for i in file2[0]]), 2))
# 1877139
