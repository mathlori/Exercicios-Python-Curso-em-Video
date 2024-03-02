# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
print('\033[35m=-=\033[m'*10)
print('\033[32mGrupo da maioridade\033[m')
print('\033[35m=-=\033[m'*10)
contador = 0
ordem = 1
for i in range(1,8):
    ano = int(input(f'\n Digite o ano de nascimento da {ordem}ª pessoa: '))
    ordem = ordem + 1
    if ano <= 2005:
        contador += 1
print(f'\n São, ao todo, {contador} pessoas na maioridade e {i - contador} que são menores de idade ')

