lines = open('input', 'r')
lines = lines.readlines()
lines = [line.rstrip('\n').split(' ') for line in lines]

# past lines
pl = []
# current line
cl = 0

accumulator = 0
duplicate = False

while not duplicate and cl < len(lines):
    pl.append(cl)
    if lines[cl][0] == 'acc':
        accumulator += int(lines[cl][1])
        cl += 1
    elif lines[cl][0] == 'jmp':
        cl += int(lines[cl][1])
    else:
        cl += 1
    duplicate = cl in pl

print(accumulator)
