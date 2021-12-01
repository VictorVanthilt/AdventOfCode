file = [int(line.rstrip('\n')) for line in open('AdventOfCode/2021/Dec01/input.txt', 'r').readlines()]
sum([file[i] > file[i-1] for i in range(len(file))])
