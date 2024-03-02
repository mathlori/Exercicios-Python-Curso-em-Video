# Exercício 6: Faça um programa que leia três números e mostre qual é o maior e qual é o menor
print('-='*20)
print('Análise de maior e menor número')
print('-='*20)
N1 = input('Digite um número: ')
N2 = input('Digite um número: ')
N3 = input('Digite um número: ')
lista = [N1, N2, N3]
maior = max(lista)
menor = min(lista)
print(f'O maior é {maior}, e o menor é {menor}')

