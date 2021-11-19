lines = open('input', 'r')
lines = lines.readlines()
lines = [line.rstrip('\n').split(' ') for line in lines]

def console(input):
    # past lines
    pl = []
    # current line
    cl = 0

    accumulator = 0
    duplicate = False

    while not duplicate and cl < len(lines):
        duplicate = cl in pl
        pl.append(cl)

        if input[cl][0] == 'acc':
            accumulator += int(input[cl][1])
            cl += 1
        elif input[cl][0] == 'jmp':
            cl += int(input[cl][1])
        else:
            cl += 1

    return(duplicate, accumulator, cl)

for index, koppel in enumerate(lines):
    newlines = open('input', 'r')
    newlines = newlines.readlines()
    newlines = [line.rstrip('\n').split(' ') for line in newlines]
    if koppel[0] == 'jmp':
        newlines[index][0] = 'nop'
        response = console(newlines)

    elif koppel[0] == 'nop':
        newlines[index][0] = 'jmp'
        response = console(newlines)
    else: response = (True, )
    if not response[0]:
        print(response, index)
    newlines.clear()
