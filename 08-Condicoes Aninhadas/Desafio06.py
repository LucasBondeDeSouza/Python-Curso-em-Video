# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

ano_nascimento = int(input('Ano de Nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: JUNIOR')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')