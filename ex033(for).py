# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('\033[35m=-=\033[m'*10)
print('\033[32mNúmeros Ímpares.\033[m')
print('\033[35m=-=\033[m'*10)

for c in range(1,51):
    print(' ',end='')
    if c%2 == 0:
     print(c,end='')