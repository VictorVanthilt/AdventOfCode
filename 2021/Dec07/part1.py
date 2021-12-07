file = [int(i) for i in open('input.txt', 'r').readline().rstrip().split(',')]
spendage = []
for i in range(min(file), max(file) + 1):
    fuel = 0
    for crab in file:
        fuel += abs(crab - i)
    spendage.append((fuel, i))
print(min(spendage))
