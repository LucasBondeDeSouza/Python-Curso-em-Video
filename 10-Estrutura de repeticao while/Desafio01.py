# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe seu sexo: [M/F] ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper()

print('Sexo {} registrado com sucesso'.format(sexo))