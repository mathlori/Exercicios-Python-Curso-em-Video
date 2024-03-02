def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso.")

def leArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro na leitura.")
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"Nome: {dado[0]: <30} Idade {dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arquivo, nome = "Desconhecido", idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        try:
            a.write(f'{nome}, {idade}\n')
        except:
            print("Houve um erro na passagem dos dados para o arquivo.")