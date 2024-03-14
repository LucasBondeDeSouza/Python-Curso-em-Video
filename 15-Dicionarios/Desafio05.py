# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicinários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

pessoa = {}
grupo = []

soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').upper()

    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())

    escolha = input('Quer continuar? [S/N] ').upper()
    while escolha not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        escolha = input('Quer continuar? [S/N] ').upper()
    
    if escolha == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')

media = soma / len(grupo)
print(f'B) A média de idade é de {media:5.2f} anos.')

print(f'C) As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')

print()

print(f'D) Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')