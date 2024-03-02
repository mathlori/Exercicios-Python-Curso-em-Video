# Exercício 6: Faça um programa que leia um nome completo e separe o primeiro e o último nome.

completo = input('Insira um nome completo: ')
dividido = completo.split()
print(f'O primeiro nome é {dividido[0]}, o último é {dividido[(len(dividido) - 1)]} ')