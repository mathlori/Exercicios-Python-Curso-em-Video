"""Faça um programa que receba vários valores como parâmetro e analise qual o maior através de uma função criada chamada maior()"""

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função maior()")


def maior(*nums):
    maior = None
    for i in nums:
        if i > maior:
            maior = i

    print("Foram informados", len(nums), "valores" , "O maior  deles é", maior)