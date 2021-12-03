import numpy as np
file = [i.rstrip() for i in open('input.txt', 'r').readlines()]
file = np.array([[int(i) for i in j] for j in file])


def get_rates(data):
    gam = ''
    for i in range(12):
        if sum(file[:,i]) > 500:
            gam += '1'
        else:
            gam += '0'
    return int(gam, 2), 2**12 - 1 - int(gam, 2)

print(get_rates(file)[0]*get_rates(file)[1])
# 2003336
