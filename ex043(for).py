# Exercício: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
import math as m
print('\033[35m=-=\033[m'*10)
print('\033[35m=Maior e menor da sequência\033[m')
print('\033[35m=-=\033[m'*10)
maior = 0
menor = m.inf 

for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}º pessoa'))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')