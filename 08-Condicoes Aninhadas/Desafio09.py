# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 'preço normal' e 'condição de pagamento':

# À vista dinheiro / cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

escolha = int(input('Qual é a opção? '))

if escolha == 1:
    novo_preco = preco - preco * 0.10
elif escolha == 2:
    novo_preco = preco - preco * 0.05
elif escolha == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif escolha == 4:
    qnt_parcelas = int(input('Quantas parcelas? '))
    novo_preco = preco + preco * 0.20
    parcela = novo_preco / qnt_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qnt_parcelas, parcela))
else:
    print('Opção Inválida. Tente Novamente!')    

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, novo_preco))