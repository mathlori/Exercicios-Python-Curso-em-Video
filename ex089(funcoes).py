"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o idade de nascimento de uma pessoa, retornando um
 valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""


def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função voto()")

def voto(ano):
    from datetime import date
    
    hj = date.today().year
    idade = hj - ano

    if idade < 18 and idade >= 16:
        return "VOTO OPCIONAL"
    elif idade < 16:
        return "VOTO NEGADO"
    else:
        return "VOTO OBRIGATORIO"

idade = int(input("Ano de nascimento: "))
voto = voto(idade)

print(voto)