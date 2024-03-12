# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

valores = []
pares = []
impares = []

while True:
    numeros = int(input('Digite um número: '))
    valores.append(numeros)

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print('-=' * 20)
print(f'A lista completa é {valores}')

for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')