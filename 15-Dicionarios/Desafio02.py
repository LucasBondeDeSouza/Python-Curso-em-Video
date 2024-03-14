# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = dict()

for c in range(1, 5):
    dado = randint(1, 6)
    jogadores[f'jogador{c}'] = dado

print('valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)