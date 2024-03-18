# Crie um pacote chamado 'utilidadesCeV' que tenha dois módulos internos chamados 'moeda' e 'dado'.

# Transfira todas as funções utilizadas nos desafios 01, 02 e 03 para o primeiro pacote e matenha tudo funcionando.

from utilidades.moeda import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)