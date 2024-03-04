# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

from random import choice

aluno1 = input('DIgite o nome do 1° aluno: ')
aluno2 = input('DIgite o nome do 2° aluno: ')
aluno3 = input('DIgite o nome do 3° aluno: ')
aluno4 = input('DIgite o nome do 4° aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = choice(alunos)

print('O aluno sorteado foi o(a) {}'.format(aluno_sorteado))