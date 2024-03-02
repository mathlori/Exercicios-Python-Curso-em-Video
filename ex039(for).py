# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
print('\033[35m=-=\033[m'*10)
print('\033[32mDetector de Palíndromos\033[m')
print('\033[35m=-=\033[m'*10)
a = input('\nDigite algo: ').upper().strip()
a = a.replace(' ', '')
print('O contrário de ', a,' é', a[::-1])
if a == a[::-1]:
    print('Palavra digitada é um palíndromo')
else:
    print('Palavra digitada não é um palíndromo')

