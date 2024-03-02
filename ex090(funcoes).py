"""Crie um programa que contenha uma função fatorial() com dois parâmetros, um número, e se deve ou não mostrar na tela o resultado após
 a função"""    

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função fatorial()")

def fatorial(num, mostra):
    f = 1
    for i in range(num, 1, -1):
        if mostra:
            if i > 1:
                print(i, end = 'x')
            else:
                print(i, end = '=')
        f *= i
        return f

