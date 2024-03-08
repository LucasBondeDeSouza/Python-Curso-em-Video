# Cie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
idade = 0

for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))

    idade = ano_atual - nascimento

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))