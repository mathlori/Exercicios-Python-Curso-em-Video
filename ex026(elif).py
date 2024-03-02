# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
print('\033[32m=-=\033[m'*10)
print('\033[35mCálculo de médias\033[m')
print('\033[32m=-=\033[m'*10)
n1 = float(input('\nDigite uma nota: '))
n2 = float(input('\nDigite outra nota: '))
media = (n1+n2)/2
print(f'\nMédia: {media}, portanto:')
if media < 5.0:
    print('Reprovado.')
elif 5 <= media <= 6.9:
    print('Recuperação.')
else:
    print('Aprovado.')
