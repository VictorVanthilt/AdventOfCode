def count_trees(file):
    file = open(file, 'r')
    file = [line.rstrip('\n') for line in file.readlines()]
    index, trees, modulo = 0 , 0, len(file[0])
    for line in file:
        if line[index % modulo] == '#':
            trees += 1
        index += 3
    return trees

print(count_trees('slope.txt'))
