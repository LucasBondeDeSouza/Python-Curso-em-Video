# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal

numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção Inválida. Tente Novamente!')