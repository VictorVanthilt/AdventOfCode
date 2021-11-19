# fuel : mass / 3 round down - 2
input = [int(line.rstrip('\n')) // 3 - 2 for line in open('input', 'r').readlines()]
print(sum(input))

# 3256114
