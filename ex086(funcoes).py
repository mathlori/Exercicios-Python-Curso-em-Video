"""Faça uma função contador que recebe início, fim e passo. No final, realizando uma contagem de 1 a 10 (de 1 em 1), de 10 a 0 (de 2 
em 2) e uma personalizada"""

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)


titulo("Função Contador()")

from time import sleep

def contador(inicio, fim, passo):

    if inicio > fim:
        passo = -passo
    
    for i in range(inicio, fim + passo, passo):
        print(i)
        sleep(1)

contador(1, 10, 1)
print()
contador(10, 0, 2 )

init = int(input("Início: "))
fim = int(input("Fim: "))
pac = int(input("Passo: "))