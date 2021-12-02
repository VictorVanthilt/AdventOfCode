file = [i.rstrip('\n').split(' ') for i in open('input.txt', 'r').readlines()]

aim, hor, ver = 0, 0, 0
for line in file:
    if line[0] == 'forward':
        hor += int(line[1])
        ver += aim*int(line[1])
    elif line[0] == 'up': aim -= int(line[1])
    elif line[0] == 'down': aim += int(line[1])

print(hor*ver)
# 1544000595
