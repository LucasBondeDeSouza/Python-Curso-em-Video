# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UM PA')
print('=' * 20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print('{} '.format(c), end='-> ')

print('ACABOU')