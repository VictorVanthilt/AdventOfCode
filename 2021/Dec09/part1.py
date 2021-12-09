# THIS CODE WAS STOLEN FROM u/wleftwich on reddit
from collections import deque

with open('input.txt') as fh:
    data = fh.read()

grid = {}
for y, line in enumerate(data.split()):
    for x, c in enumerate(line):
        grid[complex(x, -y)] = int(c)

def iter_neighbors(coord, grid=grid):
    for delta in [1, 0+1j, -1, 0-1j]:
        p = grid.get(coord + delta)
        if p is not None:
            yield p

# part 1

total_risk = 0
for (coord, p) in grid.items():
    if p < min(iter_neighbors(coord)):
        total_risk += p + 1
part_1 = total_risk
print('part_1 =', part_1)
