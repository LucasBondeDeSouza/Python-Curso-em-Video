# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno["media"] <= 5.0:
    aluno['situacao'] = 'Reprovado'
elif aluno["media"] < 7.0:
    aluno['situacao'] = 'Recuperação'
elif aluno["media"] >= 7.0:
    aluno['situacao'] = 'Aprovado'

print('-=' * 30)

for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')