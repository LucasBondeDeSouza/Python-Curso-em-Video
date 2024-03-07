# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

opcoes = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(opcoes)

print('Sua opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha_jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if escolha_jogador == 0:
    player = 'Pedra'
elif escolha_jogador == 1:
    player = 'Papel'
elif escolha_jogador == 2:
    player = 'Tesoura'
else:
    print('Opção Inválida. Tente Novamente!')

print('-=-' * 10)
print('Computador jogou {}'.format(pc))
print('Jogador jogou {}'.format(player))
print('-=-' * 10)

if player == 'Papel' and pc == 'Pedra' or player == 'Pedra' and pc == 'Tesoura' or player == 'Tesoura' and pc == 'Papel':
    print('JOGADOR VENCE')
elif pc == 'Papel' and player == 'Pedra' or pc == 'Pedra' and player == 'Tesoura' or pc == 'Tesoura' and player == 'Papel':
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')