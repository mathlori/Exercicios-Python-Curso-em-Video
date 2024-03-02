print('\033[35m=-=\033[m'*10)
print('\033[32mFibonacci\033[m')
print('\033[35m=-=\033[m'*10)

"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""

n = int(input('Digite o enésimo termo da sequência: '))
cont = 3
t1 = 0
t2 = 1

print(f'{t1} => {t2}', end = '')

while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print (f' => {t3}', end = '')
    cont += 1
   
    