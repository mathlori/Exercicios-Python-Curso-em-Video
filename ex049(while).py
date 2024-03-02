print('\033[35m=-=\033[m'*10)
print('\033[32mProgressão Aritmética\033[m')
print('\033[35m=-=\033[m'*10)

'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
 a estrutura while.'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
print(a1, end = ', ')
while cont != 10:
    a1 += r
    print(a1, end = ', ')
    cont += 1