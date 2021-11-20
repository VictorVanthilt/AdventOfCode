input = open('input', 'r').readlines()
input = tuple([int(i) for i in input[0].rstrip('\n').split(',')])

def playGame(game):
    i = 0
    while game[i] in (1, 2):
        if game[i] == 1:
            game[game[i + 3]] = game[game[i + 1]] + game[game[i + 2]]
        else:
            game[game[i + 3]] = game[game[i + 1]] * game[game[i + 2]]
        i += 4

    return game[:3]

for l in range(100):
    for m in range(100):
        newinput = [i for i in input]
        newinput[1] = l
        newinput[2] = m
        response = playGame(newinput)
        if response[0] == 19690720: print(response)
