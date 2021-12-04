import numpy as np
file = open('input.txt', 'r')
numbers = [int(j) for j in file.readline().rstrip().split(',')]

file.readline()
line = '1'

# make boards
board, boards = [], []
while line:
    line = file.readline()
    if line != '\n':
        board.append([int(j) for j in line.rstrip().split(' ') if j != ''])
    else:
        boards.append(board)
        board = []

boards.append(board[:-1])
def get_last_winner(boards):
    winners = []
    pulls = []
    i=0
    for i in range(len(numbers)):
        pulled = numbers[:i+1]
        for board in boards:
            for row in board:
                if set(row).issubset(set(pulled)):
                    if board not in winners:
                        winners.append(board)
                        pulls.append(pulled)
            for row in np.array(board).T:
                if set(row).issubset(set(pulled)):
                    if board not in winners:
                        winners.append(board)
                        pulls.append(pulled)


    return winners, pulls

winner, pulls = get_last_winner(boards)
winner = np.array(winner[-1])
for number in pulls[-1]:
    winner[winner == number] = 0

print(sum(sum(winner)) * pulls[-1][-1])
