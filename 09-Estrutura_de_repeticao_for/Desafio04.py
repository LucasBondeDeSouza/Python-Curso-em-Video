# Refaça o desafio mostrando a Tabuada de um número que o usuário escolher. Só que agora utilizando um laço for.

numero = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    resultado = numero * c
    print('{} x {:2} = {}'.format(numero, c, resultado))