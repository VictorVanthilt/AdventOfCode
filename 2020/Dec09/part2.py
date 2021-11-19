file = open('input', 'r')
file = file.readlines()
file = [int(line) for line in file]

answer = 41682220

for i in range(len(file)):
    j = 0
    som = 0
    while som < answer:
        som = sum(file[i:j])
        if som == answer and file[i:j] != [answer]:
            print(min(file[i:j]) + max(file[i:j]))
            break
        j += 1
