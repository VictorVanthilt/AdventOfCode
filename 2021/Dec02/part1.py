file = [i.rstrip('\n').split(' ') for i in open('input.txt', 'r').readlines()]

hor, ver = 0, 0
for line in file:
    if line[0] == 'forward': hor += int(line[1])
    elif line[0] == 'up': ver -= int(line[1])
    elif line[0] == 'down': ver += int(line[1])

print(hor*ver)
# 1727835
