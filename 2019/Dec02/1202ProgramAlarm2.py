19690720
input = open('input', 'r').readlines()
input = [int(i) for i in input[0].rstrip('\n').split(',')]
# still broken!
def getWords(input, j, k):
    i = 0
    input[1] = j
    input[2] = k
    while input[i] in (1, 2):
        if input[i] == 1:
            input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
        else:
            input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
        i += 4
    print(input[:4])
    return input[1], input[2]

for j in range(0, 100):
    for k in range(0, 100):
        print(input[0])
        noun, verb = getWords(input, j, k)
        if 100*noun + verb == 19690720:
            print(i, j)
            # break
    # break
