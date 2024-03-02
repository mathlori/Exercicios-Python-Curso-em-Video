# Exercício 14: Escreva um programa que o computador pense um número de 1 a 5, em que o usuário deve adivinhar esse. O
# programa deve mostrar se o usuário acertou ou errou.
print('-='*20)
print('Adivinhação de números')
print('-='*20)

import random
na = random.randint(0,5)
ne = int(input('Que número acha que eu escolhi? É de 0 a 5? '))
if ne == na:
    print(f'Parabéns, eu havia pensado no número {na} mesmo!')

else:
    print(f'Você errou... O número que você escolheu foi {ne}, e eu havia pensado em {na}')
print('-----------------------------')




