pop = [0]*9
file = [int(i) for i in open('input.txt', 'r').readline().split(',')]
for i in file:
    pop[i] += 1

for _ in range(256):
    newPop = [0]*9
    for i in range(1, 9):
        newPop[i-1] = pop[i]
    newPop[8] = pop[0]
    newPop[6] += pop[0]

    pop = newPop

print(sum(pop))
# way faster than part1!
