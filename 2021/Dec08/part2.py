from itertools import permutations

lines = [line.rstrip().split(' | ') for line in open('input.txt', 'r').readlines()]
display = {'abcefg' : '0', 'cf' : '1', 'acdeg' : '2', 'acdfg' : '3', 'bcdf' : '4', 'abdfg' : '5', 'abdefg' : '6', 'acf' : '7', 'abcdefg' : '8', 'abcdfg' : '9'}

tables = [perm.maketrans('abcdefg', perm) for perm in [''.join(p) for p in permutations('abcdefg')]]
count = 0
for line in lines:
    for table in tables:
        if set([''.join(sorted(i)) for i in line[0].translate(table).split(' ')]) == set(display.keys()):
            count += int(''.join([display[''.join(sorted(i))] for i in line[1].translate(table).split(' ')]))
print(count)
