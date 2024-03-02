#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('\033[35m=-=\033[m'*10)
print('\033[32mGerenciador de Pagamentos.\033[m')
print('\033[35m=-=\033[m'*10)
valor = float(input('\nQual o valor a ser pago?: '))
forma1 = valor * 0.9
forma2 = valor * 0.95
forma3 = valor
forma4 = valor * 1.2
opc = [forma1, forma2, forma3, forma4]
print('\nEssas são as opções: \n [1] à vista no dinheiro ou cheque: 10% de desconto.\n [2] à vista no cartão:',end='')
print('5% de desconto\n [3] em até 2x no cartão: preço normal\n [4] em 3x ou mais no cartão: 20% de juros')
escolha = int(input('\nQual dessas opções você prefere?: '))
if escolha == 1:
    print(f'\nCom essa opção, o valor será de {forma1}.')
elif escolha == 2:
    print(f'\nCom essa opção, o valor será de {forma2}.')
elif escolha == 3:
    print(f'\nCom essa opção, o valor será de {forma3}.')
elif escolha == 4:
    print(f'\nCom essa opção, o valor será de {forma4}')
else:
    print('Erro, reinicie o código.')