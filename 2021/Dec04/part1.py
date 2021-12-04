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
        boards.append(np.array(board))
        board = []

boards.append(np.array(board[:-1]))

def get_winner(boards):
    i=0
    for i in range(len(numbers)):
        pulled = numbers[:i+1]
        for board in boards:
            for row in board:
                if set(row).issubset(set(pulled)):
                    return board, pulled
            for row in board.T:
                if set(row).issubset(set(pulled)):
                    return board, pulled


winner, numbers = get_winner(boards)
for number in numbers:
    winner[winner == number] = 0

print(sum(sum(winner)) * numbers[-1])
