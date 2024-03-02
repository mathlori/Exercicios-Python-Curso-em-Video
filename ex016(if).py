# Exercício 3: Crie um programa que leia um número inteiro e verifique se ele é par ou impar
print('-='*20)
print('Par ou ímpar?')
print('-='*20)
number = int(input('Insira um número: '))
if number % 2 == 0:
    print(f'{number} é um número par')
else:
    print(f'{number} é um número ímpar.')
print('-----------------------------')

