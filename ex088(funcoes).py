'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função ante-
 rior.'''

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Funções sorteia() e somaPar()")

from random import randint

nums = list()

def sorteia(n):
    cont = 0
    while cont != 5:
        n.append(randint(1,10000))
        cont += 1
    print("Números sorteados: ", end = ' ')
    for i in n:
        print(i, end = ' ')

def somaPar(n):
    soma = 0
    for i in n:
        if i % 2 == 0:
            soma += i
    print("\nA soma é", soma)


sorteia(nums)
somaPar(nums)