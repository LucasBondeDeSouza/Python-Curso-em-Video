# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitado, em ordem crescente.

valores = []

while True:
    numeros = int(input('Digite um valor: '))

    if numeros not in valores:
        valores.append(numeros)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')