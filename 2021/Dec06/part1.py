file = [int(i) for i in open('input.txt', 'r').readline().split(',')]

for _ in range(80):
    newfish = []
    for i, fish in enumerate(file):
        if fish:
            file[i] -= 1
        else:
            newfish.append(8)
            file[i] = 6
    file += newfish

print(len(file))
