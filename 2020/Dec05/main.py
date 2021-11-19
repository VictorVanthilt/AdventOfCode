file = open('copy', 'r')
file = file.readlines()
file = [line.rstrip('\n') for line in file]

def finder(bottom, top, string):
    seats = [i for i in range(bottom, top + 1)]
    for char in string:
        n = len(seats) // 2
        if char == 'F':
            seats = seats[:n]
        else:
            seats = seats[n:]
    return seats[0]

ids = []
for line in file:
    ids.append(finder(0, 127, line[:7]) * 8 + finder(0, 7, line[7:]))
     
ids.sort()
ids = set(ids)
allseats = set([i for i in range(1016)])
print(allseats.difference(ids))
