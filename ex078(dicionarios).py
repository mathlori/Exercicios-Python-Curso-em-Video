'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da 
estrutura na tela.'''


print('\033[35m=-=\033[m'*10)
print('\033[32mDicionários em Python\033[m')
print('\033[35m=-=\033[m'*10)


aluno = dict()
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['média'] = float(input("Digite a média do aluno: "))

for t, v in aluno.items():
    print(t, '=', v)

if aluno['média'] >= 6:
    print(aluno['nome'], 'passou.')
else:
    print(aluno['nome'], 'não passou')