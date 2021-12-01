file = [int(line.rstrip('\n')) for line in open('input.txt', 'r').readlines()]
print(sum([file[i] > file[i-1] for i in range(len(file))]))
