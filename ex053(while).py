print('\033[35m=-=\033[m'*10)
print('\033[32mMaior e menor valor\033[m')
print('\033[35m=-=\033[m'*10)

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi
 o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
import math as m

parar = 1
maior = 0 - m.inf
menor = m.inf
resposta = str('')
cont = 0
soma = 0

while parar != 0:

    num = int(input('Digite um número: '))
    cont += 1
    soma += num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    resposta = input('Quer continuar [S/N]?: ').upper().strip() [0]
    if resposta in 'Nn':
        parar = 0

print(f'Certo, o maior número que você digitou foi {maior}, enquanto o menor foi {menor}, a média foi {soma/cont} ')