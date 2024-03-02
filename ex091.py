"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele 
marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função ficha()")

def ficha(nome = "Não informado", gols = "Não informado"):
    print('=-=' * 5)
    print('Nome do Jogador:', nome)
    print('Gols marcados:', gols)
    print('=-=' * 5)

# Principal

name = str(input("Jogador:"))
gols = str(input("Gols marcados: "))

if gols.isnumeric():
    gols = int(gols)
else:
    ficha(name)

if name.strip() == '':
    ficha(gols = gols)
else:
    ficha(name, gols)