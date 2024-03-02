# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.
print('\033[32m=-=\033[m'*10)
print('\033[35mAnálise de empréstimos\033[m')
print('\033[32m=-=\033[m'*10)
casa = float(input('\n• Quanto custa o imóvel?: '))
salario = float(input('• Quanto você ganha por mês?: '))
anos = float(input('• Em quantos anos você quer pagar?: '))
if casa/(anos*12) > salario*0.3:
    print(f'\n ➜ Em \033[1;36m{anos} anos\033[m, você pagaria {casa/(anos*12):.2f} mensalmente, o que excede 30% do seu salário, que é \n \033[33m{salario}\033[m, portanto, empréstimo \033[4;31mnegado\033[m.')
else:
    print(f'\n ➜ Em \033[1;36m{anos} anos\033[m, você pagaria {casa/(anos*12):.2f} mensalmente, o que não excede 30% do seu salário, que é \n \033[33m{salario}\033[m, portanto, empréstimo \033[4;32maprovado\033[m.')