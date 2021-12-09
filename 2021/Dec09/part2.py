# THIS CODE WAS STOLEN FROM u/wleftwich on reddit
from collections import deque

with open('input.txt') as fh:
    data = fh.read()
grid = {}
for y, line in enumerate(data.split()):
    for x, c in enumerate(line):
        grid[complex(x, -y)] = int(c)

def bfs(p, space):
    q = deque([p])
    visited = {p}
    while q:
        c = q.popleft()
        for delta in [1, 0+1j, -1, 0-1j]:
            n = c + delta
            if n in visited:
                continue
            try:
                space.remove(n)
            except KeyError:
                continue
            visited.add(n)
            q.append(n)
    return len(visited)


space = {k for k, v in grid.items() if v != 9}
basins = []
while space:
    p = space.pop()
    basins.append(bfs(p, space))

part_2 = 1
for x in sorted(basins)[-3:]:
    part_2 *= x
print('part_2=', part_2)
