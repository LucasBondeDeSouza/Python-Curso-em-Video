# Crie um programa que leia dois valores e mostre um menu na tela: 

# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
maior = 0

while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')

    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
        print('-==-' * 10)
        sleep(1)
        opcao = 0
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
        print('-==-' * 10)
        sleep(1)
        opcao = 0
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        print('-==-' * 10)
        sleep(1)
        opcao = 0
    elif opcao == 4:
        print('Infome os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('-==-' * 10)
        sleep(1)
        opcao = 0
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('-==-' * 10)
    else:
        print('Opção inválida. Tente novamente')
        print('-==-' * 10)
print('Fim do programa! Volte sempre!')