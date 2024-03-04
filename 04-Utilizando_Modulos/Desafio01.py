# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua posição inteira
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

from math import trunc

numero = float(input('Digite um valor: '))

print('A parte inteira de {} é {}'.format(numero, trunc(numero)))