print('\033[35m=-=\033[m'*10)
print('\033[32mJan Ken Po!.\033[m')
print('\033[35m=-=\033[m'*10)
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0,2)
print('[0] Pedra\n[1] Papel\n[2] Tesoura')
escolha = int(input('Faça sua escolha: '))
print('\nJAN')
sleep(1)
print('\nKEN')
sleep(1)
print('\nPOOO!')
sleep(1)

if cpu == 0:
    if escolha == 0:
        print('\nAmbos jogaram pedra, deu empate.')
    elif escolha == 1:
        print('\nVocê jogou papel e o CPU jogou pedra, você ganhou.')
    elif escolha == 2:
        print('\nVocê jogou tesoura e o CPU jogou pedra, você perdeu.')
    else:
        print('\nJogada inválida.')

if cpu == 1:
    if escolha == 0:
        print('\nVocê jogou pedra e a CPU jogou papel, você perdeu.')
    elif escolha == 1:
        print('\nAmbos jogaram papel, deu empate.')
    elif escolha == 2:
        print('\nVocê jogou tesoura e a CPU jogou papel, você ganhou.')
    else:
        print('\nJogada inválida.')

if cpu == 2:
    if escolha == 0:
        print('\nVocê jogou tesoura e a CPU jogou pedra, você perdeu.')
    elif escolha == 1:
        print('\nVocê jogou tesoura e a CPU jogou papel, você ganhou.')
    elif escolha == 2:
        print('\nAmbos jogaram tesoura, deu empate.')
    else:
        print('\nJogada inválida.')
