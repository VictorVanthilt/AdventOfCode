file = [int(line.rstrip('\n')) for line in open('2021/Dec01/input.txt', 'r').readlines()]

difflist = []

for i in range(len(file)):
    difflist.append(file[i] > file[i-1])
    
print(sum(difflist[1:]))