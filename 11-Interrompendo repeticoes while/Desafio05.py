# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = mais_de_mil = preco_barato = cont = 0
nome_barato = ''

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1

    if preco > 1000:
        mais_de_mil += 1

    if cont == 1 or preco < preco_barato:
        preco_barato = preco
        nome_barato = produto

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print('-' * 10 + ' FIM DO PROGRAMA ' + '-' * 10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_de_mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${preco_barato:.2f}')