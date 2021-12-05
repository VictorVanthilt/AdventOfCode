import numpy as np
file = [line.rstrip() for line in open('input.txt', 'r').readlines()]

lines = []
for line in file:
    split = line.split(' -> ')
    lines.append([[ int(i) for i in split[0].split(',')], [int(i) for i in split[1].split(',')]])

def yieldLine(line):
    x1, y1 = line[0]
    x2, y2 = line[1]

    xrange = [x1, x2]
    xrange.sort()
    xrange[1] += 1

    yrange = [y1, y2]
    yrange.sort()
    yrange[1] += 1
    dx, dy = x2 - x1, y2 - y1
    if dy:
        for y in range(*yrange):
            yield int(dx/dy * (y - y1) + x1), y
    else:
        for x in range(*xrange):
            yield x, y1

size = np.max(np.unique(lines))
map = np.zeros((size + 1, size + 1))

for line in lines:
    for coord in yieldLine(line):
        map[coord[0], coord[1]] += 1
print(map.T)
print(np.size(map[map > 1]))
