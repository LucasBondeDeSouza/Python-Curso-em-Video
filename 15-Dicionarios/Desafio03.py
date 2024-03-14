# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

pessoa = {}

pessoa['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.datetime.now().year
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - ano_atual)

print('-=' * 30)

for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')