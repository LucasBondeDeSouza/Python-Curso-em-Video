# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 

# A) Quantas pessoas foram cadastrados.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
temp = []
maior_peso = menor_peso = 0

while True:
    nome = input('Nome: ')
    temp.append(nome)
    peso = float(input('Peso: '))
    temp.append(peso)

    if len(pessoas) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        if temp[1] < menor_peso:
            menor_peso = temp[1]
    pessoas.append(temp[:])
    temp.clear()

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').upper()
    
    if escolha == 'N':
        break


print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor_peso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')