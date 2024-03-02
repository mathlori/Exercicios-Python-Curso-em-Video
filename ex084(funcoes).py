# Faça uma função que receba largura e comprimento como parâmetro e calcule a área. (Aproveita e faz uma que reproduz seu tíulo também)
def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função que calcula Área")

def area(b, h):
    area = b * h 
    return area

b = float(input("Base (b): "))
h = float(input("Altura (h): "))

area(b, h)