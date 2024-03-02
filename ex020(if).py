# Exercício 7: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salá -
# rios superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('-='*20)
print('Aumento de salários')
print('-='*20)
salario = int(input('Qual é o seu salário ?'))
if salario > 1250:
    print(f'Seu salário é maior que 1250, portanto receberá um aumento de 10%, ficando com {salario * 1.1}')
else:
    print(f'Seu salário é menor ou igual a 1250, portanto receberá um aumento de 15%, ficando com {salario * 1.15}')

