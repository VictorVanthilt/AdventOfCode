def count_trees(over, down, file):
    file = open(file, 'r')
    file = [line.rstrip('\n') for line in file.readlines()]
    line, index, trees, modulo = 0, 0 , 0, len(file[0])

    while line < len(file):
        if file[line][index % modulo] == '#':
            trees += 1
        index += over
        line += down
    return trees

print(count_trees(1, 1, 'slope.txt'))
print(count_trees(3, 1, 'slope.txt'))
print(count_trees(5, 1, 'slope.txt'))
print(count_trees(7, 1, 'slope.txt'))
print(count_trees(1, 2, 'slope.txt'))
print(70 * 240 * 68 * 67 * 37)
