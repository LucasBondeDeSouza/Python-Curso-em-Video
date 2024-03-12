valores = []
valores.append(5)
valores.append(9)
valores.append(4)
# [5, 9, 4]

'''for v in valores:
    print(f'{v}...', end='')
    5...9...4...'''

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')