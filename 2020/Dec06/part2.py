from collections import Counter as counter
lines = open('answers', 'r')
lines = lines.readlines()
lines = [line.rstrip('\n') for line in lines]

yes = 0
group = ['',0]
for line in lines:
    if line == '':
        for question in counter(group[0]).items():
            if question[1] == group[1]:
                yes += 1

        group = ['',0]
    else:
        group[0] += line
        group[1] += 1

for question in counter(group[0]).items():
    if question[1] == group[1]:
        yes += 1
print(yes)
