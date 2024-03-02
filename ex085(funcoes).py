""""Programe uma função que escreve algo e preencha com "~" em tamanho adaptável."""                                                                                                                                                                                                                                                                                                             

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função Escreva()")

def escreva(txt):
    print("~" * len(txt))
    print(txt)
    print("~" * len(txt))


msg = str(input("Mensagem: "))

escreva(msg)