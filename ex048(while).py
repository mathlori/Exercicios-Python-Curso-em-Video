print('\033[35m=-=\033[m'*10)
print('\033[32mCálculo Fatorial\033[m')
print('\033[35m=-=\033[m'*10)
"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120"""
num = int(input('Digite um número: '))
fatorial = 1
while num != 0:
    fatorial*= num
    num -= 1
print(fatorial)
