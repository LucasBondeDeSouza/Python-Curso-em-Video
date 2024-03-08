# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa. mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

soma_idade = 0
qnt_pessoas = 0
homem_velho = 0
nome_homem_velho = ''
mulheres_20anos = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    soma_idade += idade
    qnt_pessoas += 1

    if sexo == 'M' and idade > homem_velho:
        homem_velho = idade
        nome_homem_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_20anos += 1

media_idade = soma_idade / qnt_pessoas

print('A média de idade do grupo é de {:.1f} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_velho, nome_homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres_20anos))