from itertools import permutations
# amount -> number
# 2 -> 1
# 3 -> 7
# 4 -> 4
# 5 -> 2
# 5 -> 3
# 5 -> 5
# 6 -> 6
# 6 -> 9
# 7 -> 8
lines = [line.rstrip().split(' | ') for line in open('input.txt', 'r').readlines()]
# print(lines)
zero = set()
one = set('cf')
two = set('acdeg')
three = set('acdfg')
four = set('bcdf')
five = set('abdfg')
six = set('abdefg')
seven = set('acf')
eight = set('abcdefg')
nine = set('abcdfg')
display = {'abcefg' : 0, 'cf' : 1, 'acdeg' : 2, 'acdfg' : 3, 'bcdf' : 4, 'abdfg' : 5, 'abdefg' : 6, 'acf' : 7, 'abcdefg' : 8, 'abcdfg' : 9}

perms = [''.join(p) for p in permutations('abcdefg')]
for line in lines:
    for perm in perms:
        table = perm.maketrans('abcdefg', perm)
        if sum([disp.translate(table) in display for disp in line[0].split(' ')]) > 3: print(line, perm)
