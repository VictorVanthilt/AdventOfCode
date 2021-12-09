file = [line.rstrip() for line in open('test.txt', 'r').readlines()]
print(file)
risk = 0
for i in range(len(file)):
    for j in range(len(file[0])):
        if i%len(file) and j%len(file[0]):
            pass
        else:
            print(i, j)
