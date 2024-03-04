salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario * 15 / 100
novo_salario = salario + aumento

print('O salário que era de R${:.2f}, agora é R${:.2f}'.format(salario, novo_salario))