# Faça um programa que tenha uma dimensão chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {a:.1f}m²')

print(' Controle de Terreno ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
