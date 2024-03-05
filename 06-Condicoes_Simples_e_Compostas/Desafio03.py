# crie um programa que lei um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número {} é Par!'.format(numero))
else:
    print('O número {} é Ímpar!'.format(numero))