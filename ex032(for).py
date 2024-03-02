# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('\033[35m=-=\033[m'*10)
print('\033[32mContagem regressiva.\033[m')
print('\033[35m=-=\033[m'*10)

for c in range (10,-1,-1):
    sleep(1)
    print(c)
print('\033[1;35mFELIZ ANO NOVO!🎆\033[m')
