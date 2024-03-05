# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras Maiúsculas
# -> O nome com todas Minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

maiusculas = nome.upper()
minusculas = nome.lower()
total_letras = len(nome.replace(" ", ""))
primeiro_nome = len(nome.split()[0])

print('Seu nome: {}'.format(nome))
print('Seu nome com todas as letras Maiúsculas: {}'.format(maiusculas))
print('Seu nome com todas as letras Minúsculas: {}'.format(minusculas))
print('Seu nome tem {} letras'.format(total_letras))
print('Seu primeiro nome tem {} letras'.format(primeiro_nome))