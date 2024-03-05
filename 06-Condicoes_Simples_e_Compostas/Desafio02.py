# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7,00 por cada Km acima do limite. 

velocidade = float(input('Digite a velocidade do carro: '))

calculo_multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado!')
    print('O valor da multa é R${:.2f}'.format(calculo_multa))
else:
    print('Você está dentro do limite de velocidade!')