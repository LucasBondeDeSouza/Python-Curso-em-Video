# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o seu salário: R$'))

if salario > 1250.00:
    aumento = salario + ( salario * 10 / 100)
    print('Você teve um aumento de 10% no seu salário!')
    print('Seu novo salário é {:.2f}'.format(aumento))
else:
    aumento = salario + ( salario * 15 / 100)
    print('Você teve um aumento de 15% no seu salário!')
    print('Seu novo salário é {:.2f}'.format(aumento))