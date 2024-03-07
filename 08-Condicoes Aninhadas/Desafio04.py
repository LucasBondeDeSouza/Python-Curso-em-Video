# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))

if idade < 18:
    diferenca = 18 - idade
    ano_alistamento = ano_atual + diferenca
    print('Ainda faltam {} ano(s) para o alistamento.'.format(diferenca))
    print('Seu alistamento será em {}.'.format(ano_alistamento))
elif idade > 18:
    diferenca = idade - 18
    ano_alistamento = ano_atual - diferenca
    print('Você já deveria ter se alistado há {} ano(s).'.format(diferenca))
    print('Seu alistamento foi em {}.'.format(ano_alistamento))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')