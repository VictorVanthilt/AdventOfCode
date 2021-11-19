input = [int(line.rstrip('\n')) for line in open('input', 'r').readlines()]

def fuelCalc(fuel):
    return fuel // 3 - 2

total = 0

for mass in input:
    fuelneeded = fuelCalc(mass)
    while fuelneeded > 0:
        total += fuelneeded
        fuelneeded = fuelCalc(fuelneeded)
print(total)
# 4881302
