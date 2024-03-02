'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a 
validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função leiaInt()")

def leiaInt(string):
    print(string, end = '')
    elem = input()
    while not elem.isnumeric():
        elem = input(f"Valor não é inteiro. {string}")
    return elem
a = leiaInt("Digite um número: ")