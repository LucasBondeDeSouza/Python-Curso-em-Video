estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
print(brasil)
# [{'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}, {'uf': 'Santa Catarina', 'sigla': 'SC'}]

#for e in brasil:
    #print(e)
       #{'uf': 'São Paulo', 'sigla': 'SP'}
       #{'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
       #{'uf': 'Santa Catarina', 'sigla': 'SC'}

#for e in brasil:
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}')
           # O campo uf tem valor São Paulo
           # O campo sigla tem valor SP
           # O campo uf tem valor Rio Grande do Sul
           # O campo sigla tem valor RS
           # O campo uf tem valor Santa Catarina
           # O campo sigla tem valor SC

#for e in brasil:
    #for v in e.values():
        #print(v, end=' ')
    #print()
       # São Paulo SP
       # Rio Grande do Sul RS
       # Santa Catarina SC