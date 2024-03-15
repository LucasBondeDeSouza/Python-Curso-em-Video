# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

import datetime

def voto(nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - nascimento

    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO.')
    elif idade >= 16 and idade < 18 or idade > 70:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')

print('-' * 30)
ano_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_nascimento)