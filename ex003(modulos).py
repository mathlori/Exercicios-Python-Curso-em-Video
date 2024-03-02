import math
import random


# Exercício 3: Crie um programa em que o computador lê um número float e selecione sua parte inteira.

num = float(input('Selecione um número: '))
f = math.floor(num)
c = math.ceil(num)
print('----------------------------------------')
print(f'O número, arredondado para baixo é {f}, e para cima é {c}')
print('----------------------------------------')


