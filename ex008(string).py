# Exercício 8: Crie um programa que leia o nome completo de alguém e mostra o nome com todas as letras maiúsclas e minúsculas,
#quantas letras sem considerar espaços e quantas letras tem o primeiro nome

n = input('Qual é o seu nome? ').strip()
print(f'Seu nome em maiúsculas é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
print('Seu nome tem {} letras'.format(len(n) - n.count(' ')))
n1 = n.split()
print(f'Primeiro nome é {n1[0]} e tem {len(n1[0])} letras')


