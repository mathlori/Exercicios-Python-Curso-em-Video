import math
# Exercício 2: Faça um programa que calcule a hipotenusa de um triângulo retângulo a partir dos seus catetos oposto e
#adjacente

co = int(input('Quanto vale o cateto oposto?: '))
ca = int(input('Quanto vale o cateto adjacente?: '))
print('----------------------------------------')
print(f'A hipotenusa do triângulo com catetos {co} e {ca} vale {math.sqrt(co**2 + ca**2)}')
print('----------------------------------------')

