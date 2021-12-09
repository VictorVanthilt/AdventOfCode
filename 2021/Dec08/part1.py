print(sum([len(j) in (2, 3, 4, 7) for line in open('input.txt', 'r') for j in line.rstrip().split(' | ')[1].split(' ')]))
