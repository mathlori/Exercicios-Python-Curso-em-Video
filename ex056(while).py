print('\033[35m=-=\033[m'*10)
print('\033[32mJogo do Par ou Ímpar\033[m')
print('\033[35m=-=\033[m'*10)

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de 
vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

contWins = 0

while True: 
    escolha = input('Quer ser par ou ímpar?: ').upper().strip()
    if escolha == 'PAR':
        user = int(input('Digite um número de 1 a 10: '))
        cpu = randint(1, 10)
        if user + cpu % 2 == 0:
            print('Você venceu uma vez!')
            contWins += 1
        else:
            print(f'Fim de jogo. Você perdeu, mas ganhou {contWins} vezes')
            break
    elif escolha == 'ÍMPAR':
        user = int(input('Digite um número de 1 a 10: '))
        cpu = randint(1, 10)
        if user + cpu % 2 != 0:
            print('Você venceu uma vez!')
            contWins += 1
        else:
            print(f'Fim de jogo. Você perdeu, mas ganhou {contWins} vezes')
            break


