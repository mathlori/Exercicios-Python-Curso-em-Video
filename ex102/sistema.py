from lib.interface import *
from lib.arquivo import *

arq = "cursoemvideo.txt"

while True:
    if not arquivoExiste(arq):
        criarArquivo(arq)
    titulo("SISTEMA ARQUIVO VERSÃO 1.0")
    lista = ["Listar Pessoas", "Cadastrar Pessoas", "Sair"]
    opcao = menu(lista)
    match opcao:
        case 1:
            # Listar os elementos presentes em um arquivo
            leArquivo(arq)
            
        case 2:
            titulo("NOVO CADASTRO")
            nome = str(input("Nome:"))
            idade = leiaInt("Idade: ")
            cadastrar(arq, nome, idade)
        case 3:
            break


