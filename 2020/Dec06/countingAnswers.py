# per groep een set maken en dan de lengte van die sets optellen
lines = open('answers', 'r')
lines = lines.readlines()
lines = [line.rstrip('\n') for line in lines]

lengtes = []
templine = ''
for line in lines:
    if line == '':
        lengtes.append(len(set(templine)))
        templine = ''
    else:
        templine += line

lengtes.append(len(set(templine)))
print(sum(lengtes))
