# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome completo: ')

verificar_nome = "SILVA" in nome.upper()

print('Seu nome tem Silva? {}'.format(verificar_nome))