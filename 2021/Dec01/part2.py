file = [int(line.rstrip('\n')) for line in open('input.txt', 'r').readlines()]

temp1, temp2 = [], []

for i in range(len(file)-2):
    temp1.append(sum(file[i:i+3]))
    temp2.append(temp1[i] > temp1[i-1])

print(sum(temp2))
        