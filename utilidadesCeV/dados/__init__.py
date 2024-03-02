def leiaDinheiro():
    validação = False
    while validação == False:
        valor = input("Digite um valor monetário: R$ ").replace(",", ".")
        if valor.isalpha() or valor.strip() == '':
            print(f"\033[31m ERRO: {valor} é um valor inválido! \033[m ")
        else:
            validação = True
            return float(valor)

leiaDinheiro()