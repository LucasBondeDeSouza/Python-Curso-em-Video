# Aprimore o Desafio04 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
grupo_jogadores = []
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ')
    n_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, n_partidas):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    grupo_jogadores.append(jogador.copy())

    escolha = input('Quer continuar? [S/N] ').upper()
    while escolha not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        escolha = input('Quer continuar? [S/N] ').upper()
    
    if escolha == 'N':
        break
    
print('-=' * 30)
print(f'{"cod":<6}{"NOME":<15}{"GOLS":<20}{"TOTAL"}')
print('-' * 50)

for i, jogador in enumerate(grupo_jogadores):
    print(f'  {i:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]}')

while True:
    print('-' * 50)
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if busca == 999:
        break

    if busca < 0 or busca >= len(grupo_jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    elif busca <= len(grupo_jogadores):
        print(F' -- LEVANTAMENTO DO JOGADOR {grupo_jogadores[busca]["nome"]} --')
        for i, g in enumerate(grupo_jogadores[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gol(s).')
print('<<< VOLTE SEMPRE >>>')