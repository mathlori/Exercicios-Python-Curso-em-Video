print('\033[35m=-=\033[m'*10)
print('\033[32mMenu de Opções\033[m')
print('\033[35m=-=\033[m'*10)
"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
cont = 0
print(' [1] Somar\n\n [2] Multiplicar\n\n [3] Maior\n\n [4] Novos números\n\n [5] Sair do Programa')
while cont != 1:
    opcao = int(input('Digite uma opção [1,2,3,4,5]:'))
    while opcao < 1 or opcao > 5:
        opcao = int(input('Valor inválido. Digite novamente: '))
    if opcao == 1:
        print('A soma é' , num1 + num2)
    elif opcao == 2: 
        print('A multilpicação é', num1 * num2)
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior é {num1}')
        else:
            print(f'O maior é {num2}')
    elif opcao == 4:
        num1 = int(input('Certo, digite outro número:'))
        num2 = int(input('Digite outro número: '))
    elif opcao == 5:
        cont += 1
print('Encerrado')
