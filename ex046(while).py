print('\033[35m=-=\033[m'*10)
print('\033[32mJogo de adivinhação\033[m')
print('\033[35m=-=\033[m'*10)

'''Exercício: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
 tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random as r

numero = r.randint(0, 10)
num_user = int(input('Qual número o computador pensou?'))
cont = 0
while num_user != numero:
    cont += 1
    num_user = int(input('Você errou! Tente novamente: '))
print('Parabéns, você acertou! Foram necessárias ', cont + 1, 'tentativas!'  )