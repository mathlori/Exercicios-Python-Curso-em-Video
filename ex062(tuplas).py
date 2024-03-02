"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a 
listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

print('\033[35m=-=\033[m'*10)
print('\033[32mMaior e menor valor em tupla\033[m')
print('\033[35m=-=\033[m'*10)

from random import randint

tupla = randint(1,100000000000), randint(1,100000000000), randint(1,100000000000), randint(1,100000000000), (randint(1,100000000000))

print("Os números gerados são: ", tupla)

print("O maior número desses é ", max(tupla))
print("Já o menor é", min(tupla))