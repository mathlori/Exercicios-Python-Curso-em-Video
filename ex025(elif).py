# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
# idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('\033[32m=-=\033[m'*10)
print('\033[35mIdade para alistamento\033[m')
print('\033[32m=-=\033[m'*10)
ano = int(input('\n Ano de nascimento: '))

if ano == 2005:
    print('\n2023 é o ano para você se alistar!')
elif ano > 2005:
    print(f'\n2023 ainda não é o ano para você se alistar. Ainda faltam {ano - 2005} para o seu alistamento,',end='')
    print(f' que será feito em {2005 + (ano - 2005)}.')
else:
    print(f'\nVocê já devia ter se alistado a {(2023-ano)-18} anos!')