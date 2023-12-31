import sys

try:
    if sys.argv[1] == 'log':
        sys.stderr = open('results/log_error_campeonato.txt', 'w')
        sys.stdout = open('results/log_campeonato.txt', 'w')
except IndexError:
    pass

from FourInRow import FourInRow
from RandomPlayer import RandomPlayer
from ManualPlayer import ManualPlayer
from TimeCeltaPreto import CeltaPretoPlayer

players = [
    CeltaPretoPlayer(),
    RandomPlayer()
    ]
    
points = {}
for p in players:
    points[p.name()] = 0


for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[i].name() + " vs "+players[j].name())
        winner = FourInRow(players[i], players[j]).game()
        if winner == 'DRAW':
            points[players[i].name()] += 0.5
            points[players[j].name()] += 0.5
        else:
            points[winner] += 1 

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[j].name() + " vs "+players[i].name())
        winner = FourInRow(players[j], players[i]).game()
        if winner == 'DRAW':
            points[players[i].name()] += 0.5
            points[players[j].name()] += 0.5
        else:
            points[winner] += 1

print('Results:')
print('\n')
print(points)
