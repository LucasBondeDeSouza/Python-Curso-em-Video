# Crie um pequeno sistema modularizado que permita cadastrar pesoas pelo seu nome e idade em um arquivo de texto simples.

# O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e Listar todas as pessoas cadastradas.

from lib.interface.interface import *
from lib.arquivo.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')
    sleep(2)