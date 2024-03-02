print('\033[35m=-=\033[m'*10)
print('\033[32mValidação de Dados\033[m')
print('\033[35m=-=\033[m'*10)

'''Exercício: Faça um programa que leia o sexo de uma pessoa, mas só aceite como dado 'M' ou 'F', repetindo a inserção se caso 
for diferente disso.'''

sexo = input('Digite seu sexo (M ou F): ')
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor inválido, digite novamente: '))