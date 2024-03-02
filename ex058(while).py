print('\033[35m=-=\033[m'*10)
print('\033[32mEstatísticas em Produtos\033[m')
print('\033[35m=-=\033[m'*10)

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

import math as m

precoMenor = m.inf
nomeMenor = ''
total = 0
cont1k = 0

while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço desse produto: '))

    if preco < precoMenor:
        precoMenor = preco
        nomeMenor = produto
    if preco > 1000:
        cont1k += 1

    total += preco

    opc = input('Quer continuar? [S/N]: ')
    if opc in 'Nn':
        print(f'Certo. O produto mais barato é {nomeMenor}, que custa {precoMenor}. O total é {total}, e existem {cont1k} produtos\ncom preço maior do que 1000 ')
        break
    elif opc in 'Ss':
        print('Ok. Cadastrando outro produto: ')
    else:
        print('Erro.')
        break