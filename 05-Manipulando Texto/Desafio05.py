# Faça um programa que leia uma frase pelo teclado e mostre:

# -> Quantas vezes aparece a letra "A"
# -> Em que posição ela aparece a primeira vez
# -> Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').upper().strip()

letra_a = frase.count('A')
primeira_a = frase.find('A') + 1
ultima_a = frase.rfind('A') + 1

print('A letra "A" aparece {} vez(es) na frase'.format(letra_a))
print('A primeira letra "A" apareceu na posição {}'.format(primeira_a))
print('A última letra "A" apareceu na posição {}'.format(ultima_a))