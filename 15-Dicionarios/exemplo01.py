pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 21}

# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') -> O Lucas tem 21 anos

# print(pessoas.keys()) -> dict_keys(['nome', 'sexo', 'idade'])

# print(pessoas.values()) -> dict_values(['Lucas', 'M', 21])

# print(pessoas.items()) -> dict_items([('nome', 'Lucas'), ('sexo', 'M'), ('idade', 21)])

# del pessoas['sexo'] -> apaga o elemento 'sexo'

# pessoas['nome'] = 'Leandro' -> Altera o elemento 'nome' para 'Leandro'

# pessoas['peso'] = 98.5 -> Adiciona o elemento 'peso' para a variável 'pessoas'

for k, v in pessoas.items():
    print(f'{k} = {v}')
    '''nome = Lucas
       sexo = M  
       idade = 21'''