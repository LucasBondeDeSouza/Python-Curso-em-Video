# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

vitorias = 0
verifica_vencedor = ''

while True:
    computador = randint(0, 10)

    jogador = int(input('Diga um valor: '))
    par_ou_impar = input('Par ou Ímpar? [P/I] ').upper()

    if (computador + jogador ) % 2 == 0:
        verifica_vencedor = 'PAR'
    else:
        verifica_vencedor = 'ÍMPAR'

    print('-' * 35)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU {verifica_vencedor}')
    print('-' * 35)

    if verifica_vencedor == 'PAR' and par_ou_impar == 'P' or verifica_vencedor == 'ÍMPAR' and par_ou_impar == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você Perdeu!')
        break

print('=-' * 20)
print(f'GAME OVER! Você venceu {vitorias} vez(es).')