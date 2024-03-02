def aumentar(n, porcentagem, format = False):
    """A partir de dada porcentagem passada como parâmetro, a função retorna o aumento de x%"""
    return n * (100 + porcentagem)/100 if format == False else formatar(n * (100 + porcentagem)/100)

def dobro(n, format = False):
    """A função retorna o dobro do valor passado como parâmetro"""
    return n * 2 if format == False else formatar(n * 2)

def diminuir(n, porcentagem, format = False):
    """A função retorna o valor com a diminuição de x%, passado como parâmetro"""
    return n * (100 - porcentagem)/100 if format == False else formatar(n * (100 - porcentagem)/100)

def metade(n, format = False):
    """A função retorna a metade do valor passado como parâmetro"""
    return n / 2 if format == False else formatar(n/2)

def formatar(n = 0, moeda = 'R$'):
    return f"{moeda}{n:>.2f}".replace('.', ',')

def resumo(n, aumento, diminuição):
    print("=" * 10) 
    print("RESUMO")
    print("=" * 10)
    print(f"Valor informado: {formatar(n)}")
    print(f"Dobro do preço: {dobro(n, True)}")
    print(f"Metade do preço: {metade(n, True)}")
    print(f"{aumento}% de aumento: {aumentar(n, aumento, True)}")
    print(f"{diminuição}% de diminuição: {diminuir(n, diminuição, True)}")