import numpy as np
file = [line.rstrip() for line in open('input.txt', 'r').readlines()]

lines = []
for line in file:
    split = line.split(' -> ')
    lines.append([[ int(i) for i in split[0].split(',')], [int(i) for i in split[1].split(',')]])


horizontalLines = []
for line in lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        horizontalLines.append(line)

size = np.max(np.unique(horizontalLines))
map = np.zeros((size + 1, size + 1))
for line in horizontalLines:
    # [x1, y1] -> [x2, y2]
    x1, y1 = line[0]
    x2, y2 = line[1]
    xrange = [x1, x2]
    yrange = [y1, y2]
    xrange.sort()
    xrange[1] += 1
    yrange.sort()
    yrange[1] += 1
    for x in range(*xrange):
        for y in range(*yrange):
            map[x][y] += 1

# print(map.T)
print(np.size(map[map > 1]))
