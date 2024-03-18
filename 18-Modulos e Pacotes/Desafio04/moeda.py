def aumentar(preco = 0, taxa = 0, format = False):
    res = preco + (preco * taxa / 100)
    if format:
        return moeda(res)
    else:
        return res

def diminuir(preco = 0, taxa = 0, format = False):
    res = preco - (preco * taxa / 100)
    if format:
        return moeda(res)
    else:
        return res

def dobro(preco = 0, format = False):
    res = preco * 2
    if format:
        return moeda(res)
    else:
        return res

def metade(preco = 0, format = False):
    res = preco / 2
    if format:
        return moeda(res)
    else:
        return res

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco = 0, taxa_a = 10, taxa_r = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 35)
    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preco, taxa_a, True)}')
    print(f'{taxa_r}% de redução: \t{diminuir(preco, taxa_r, True)}')
    print('-' * 35)