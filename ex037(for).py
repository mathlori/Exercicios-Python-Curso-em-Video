# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.
print('\033[35m=-=\033[m'*10)
print('\033[32mProgressão Aritmética\033[m')
print('\033[35m=-=\033[m'*10)
a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
decimo = a1 + (r*10)
for i in range(a1,decimo + 1, r):
     print(f'A PA fica: {i}', end = '')