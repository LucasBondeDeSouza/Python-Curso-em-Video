# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Digite um número: '))
cont = 1
soma = num
media = num
maior = menor = num
r = 'S'

while r == 'S':
    r = input('Quer continuar? [S/N] ').upper()
    if r == 'S':
        num = int(input('Digite um número: '))
        cont += 1
        soma += num
        media = soma / cont
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print('Você digitou {} números.'.format(cont))
print('A média entre eles foi {:.2f}'.format(media))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))