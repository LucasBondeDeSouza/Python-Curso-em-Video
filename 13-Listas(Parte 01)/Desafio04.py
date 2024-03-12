# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    numeros = int(input('Digite um valor: '))
    valores.append(numeros)

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print('-=' * 20)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')