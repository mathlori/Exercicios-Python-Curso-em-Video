"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

from ex091 import titulo

titulo("Refazendo funções leiaInt() e leiaFloat()")

def leiaInt(string):

    while True:
        try:
            print(string, end = '')
            elem = int(input())
        except (ValueError, ValueError) as erro:
            print(f"\033[31m ERRO na leitura. {erro.__class__} \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mPrograma encerrado pelo usuário.\033[m")
        else:
            return elem
        
def leiaFloat(string):

    while True:
        try:
            print(string, end = '')
            elem = float(input())
        except (ValueError, ValueError) as erro:
            print(f"\033[31m ERRO na leitura. {erro.__class__} \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mPrograma encerrado pelo usuário.\033[m")
        else:
            return elem
        
x = leiaInt("Digite um número inteiro: ")
y = leiaFloat("Digite um número real: ")
print(f"O inteiro foi {x} e o real foi {y}")