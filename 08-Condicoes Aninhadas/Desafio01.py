# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
tempo_financiamento = int(input('Quantos anos de financiamento? '))

prestacao = valor_casa / (tempo_financiamento * 12)
minimo = salario_comprador * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} ano(s) a prestação será de R${:.2f}'.format(valor_casa, tempo_financiamento, prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')