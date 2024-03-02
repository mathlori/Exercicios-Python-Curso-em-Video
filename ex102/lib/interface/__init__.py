from time import sleep
def linha(tam = 42):
    print("=" * tam)

def titulo(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    titulo("Menu Principal")
    for i, e in enumerate(lista):
        print(f"\033[33mOpção {i + 1} \033[m - \033[34m {e} \033[m")
    while True:
        opc = leiaInt("\n\033[32mSelecione uma opção: \033[m")
        if opc not in (1, 2, 3, 4):
            print(f"\033[31m ERRO. Número inteiro inválido\033[m")
            continue
        else:
            return opc

def leiaInt(string):

    while True:
        try:
            print(string, end = '')
            elem = int(input())
        except (ValueError, ValueError) as erro:
            print(f"\033[31m ERRO na leitura. {erro.__class__} \033[m")
            sleep(2)
            continue
        except (KeyboardInterrupt):
            print("\033[31mPrograma encerrado pelo usuário.\033[m")
        else:
            return elem
        
