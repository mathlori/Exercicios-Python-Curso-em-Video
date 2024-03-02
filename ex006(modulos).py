import random
# Exercício 1: Faça um programa que escolha um nome de 4 presentes em uma lista

lista = ['Matheus', 'Mathias', 'Marcelo', 'Leandro']
print('----------------------------------------')
print(f'Os participantes são {lista} e o vencedor é {random.choice(lista)}')
print('----------------------------------------')

# Exercício 2: Agora faça um programa que mude a ordem da mesma lista de antes

random.shuffle(lista)
print(lista)
print('----------------------------------------')