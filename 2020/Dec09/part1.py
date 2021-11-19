file = open('input', 'r')
file = file.readlines()
file = [int(line.rstrip('\n')) for line in file]

start = 25
index = start

def check(n, slice):
    # print(slice)
    for j in slice:
        if n-j in slice and n-j != j:
            return False
    return True

for n in file[start:]:
    if check(n, file[index - 25:index]):
        print(n)
        break
    index += 1
