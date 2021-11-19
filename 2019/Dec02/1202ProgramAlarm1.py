input = open('input', 'r').readlines()
input = [int(i) for i in input[0].rstrip('\n').split(',')]
input[1] = 12
input[2] = 2

i = 0

while input[i] in (1, 2):
    if input[i] == 1:
        input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
    else:
        input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
    i += 4

print(input)
