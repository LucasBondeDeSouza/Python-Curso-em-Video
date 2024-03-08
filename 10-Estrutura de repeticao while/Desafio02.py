# Melhore o jogo onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num_sorteado = randint(0, 10)
tentativa = 0
acertou = False

print('Sou seu computador...')
print('Será que você consegue advinhar qual foi?')
palpite = 0

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    tentativa += 1
    
    if palpite == num_sorteado:
        acertou = True
    else:
        if palpite < num_sorteado:
            print('Mais... Tente mais uma vez.')
        elif palpite > num_sorteado:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tentativa))