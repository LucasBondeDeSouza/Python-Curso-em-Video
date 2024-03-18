# Dentro do pacote 'utilidadesCeV' que criamos no 'Desafio05', temos um módulo chamado 'dado'. Crie uma função chamada 'leiaDinheiro()' que seja capaz de funcionar como a função 'input()', mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidades.moeda import moeda
from utilidades.dado import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)