# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('\033[32m=-=\033[m'*10)
print('\033[35mConversor de números\033[m')
print('\033[32m=-=\033[m'*10)
numero = int(input('\n • Digite um número: '))
print('[\033[33m1\033[m] Conversão para número \033[4;33mbinário\033[m')
print('[\033[32m2\033[m] Conversão para número \033[4;32moctal\033[m')
print('[\033[34m3\033[m] Conversão para número \033[4;34mhexadecimal\033[m')
escolha = int(input('\nEscolha uma das opções: '))
if escolha == 1:
    print(f'\nO número {numero} convertido para o sistema \033[4;33mbinário\033[m é {bin(numero)}')
elif escolha == 2:
    print(f'\nO número {numero} convertido para o sistema \033[4;32moctal\033[m é {oct(numero)}')
elif escolha == 3:
    print(f'\nO número {numero} convertido para o sistema \033[4;34mhexadecimal\033[m é {hex(numero)}')
else:
    print('A escolha só pode ser 1, 2, ou 3.')