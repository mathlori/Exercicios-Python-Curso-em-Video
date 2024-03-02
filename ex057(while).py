print('\033[35m=-=\033[m'*10)
print('\033[32mValidação dos Dados\033[m')
print('\033[35m=-=\033[m'*10)   

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

cont18 = 0
contF20 = 0
contMan = 0

while True:
    sexo = input('Digite seu sexo [M/F]: ')
    idade = int(input('Digite sua idade: '))

    if idade >= 18: # Maior de 18?
        cont18 += 1
    if sexo in 'Mm': # Homem?
        contMan += 1
    if sexo in 'Ff' and idade <= 20:
        contF20 += 1
    
    opc = input('Quer continuar? [S/N]: ')
    if opc in 'Nn':
        print(f'Certo. Há {cont18} maiores de 18, {contMan} homens, e {contF20} mulheres menores de 20 anos')
        break
    elif opc in 'Ss':
        print('Ok. Carregando outro cadastro...')
    else:
        print('Erro.')
        break

    


