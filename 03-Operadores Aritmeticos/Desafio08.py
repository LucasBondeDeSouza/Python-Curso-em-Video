preco = float(input('Digite o preço do produto: '))
desconto = preco * 5 / 100
novo_preco = preco - desconto

print('R${:.2f} com 5% de desconto é R${:.2f}'.format(preco, novo_preco))