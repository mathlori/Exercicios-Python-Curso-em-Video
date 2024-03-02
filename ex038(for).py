# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('\033[35m=-=\033[m'*10)
print('\033[32mNúmeros Primos.\033[m')
print('\033[35m=-=\033[m'*10)
n = int(input('\nDigite um número: '))
contador = 0
for i in range(1,n+1):
    if n % i == 0:
        print(f'\033[32m{i}\033[m ', end = '')
        contador = contador + 1
    else:
        print(f'\033[31m{i}\033[m ', end = '')
if contador == 2:
    print(f'O numero {n} é divisível por 2 números apenas, então ele é primo. ')
else:
    print(f'O número {n} é divisível por mais de 2 números, então ele não é primo.')