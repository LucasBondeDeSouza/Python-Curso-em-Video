# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e ostre a ordem sorteada.

from random import shuffle

aluno1 = input('DIgite o nome do 1° aluno: ')
aluno2 = input('DIgite o nome do 2° aluno: ')
aluno3 = input('DIgite o nome do 3° aluno: ')
aluno4 = input('DIgite o nome do 4° aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(alunos)

print('A ordem de apresentação será: ')
print(alunos)