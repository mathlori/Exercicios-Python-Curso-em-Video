'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.'''

print('\033[35m=-=\033[m'*10)
print('\033[32mCarteira de trabalho\033[m')
print('\033[35m=-=\033[m'*10)

from datetime import datetime


carteira_de_trabalho = dict()
carteira_de_trabalho['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
carteira_de_trabalho['Idade'] = datetime.now().year - nasc
carteira_de_trabalho['CTPS'] = int(input('CTPS: '))
if carteira_de_trabalho['CTPS'] == 0:
    print('=' * 10)
    print('Nome:', carteira_de_trabalho['Nome'])
    print('Idade' , carteira_de_trabalho['Idade'])
    print('Valor da carteira de trabalho é 0')
else:
    carteira_de_trabalho['Ano de contratação'] = int(input("Ano de contratação: "))
    carteira_de_trabalho['Salário'] = float(input('Salário: '))
    carteira_de_trabalho['Aposentadoria'] = carteira_de_trabalho['Ano de contratação'] + 35 - nasc

    for i,v in carteira_de_trabalho.items():
        print(i, ':', v)