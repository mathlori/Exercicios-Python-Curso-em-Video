print('\033[35m=-=\033[m'*10)
print('\033[32mEstatísticas em Produtos\033[m')
print('\033[35m=-=\033[m'*10)

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser 
sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 

OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input('Digite um valor: '))

cont1 = 0
cont10 = 0
cont20 = 0
cont50 = 0

while True:

    while valor - 50 >= 0:
        valor = valor - 50
        cont50 += 1
    while valor - 20 >= 0:
        valor = valor - 20
        cont20 += 1
    while valor - 10 >= 0:
        valor = valor - 10
        cont10 += 1
    while valor - 1 >= 0:
        valor -= 1
        cont1 += 1
    if cont50 * 50 + cont20 * 20 + cont10 * 10 + cont1 * 1 != valor:
        print(f'São necessárias {cont50} notas de 50, {cont20} notas de 20, {cont10} notas de 10 e {cont1} notas de 1.')
        break
 