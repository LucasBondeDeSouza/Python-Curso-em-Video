largura = float(input('Digite a Largura(em Metros) da parede: '))
altura = float(input('Digite a Altura(em Metros) da parede: '))

area = largura * altura
litros_tinta = area / 2

print('São necessários {}L de tinta para pintar uma parede de {} m²'.format(litros_tinta, area))