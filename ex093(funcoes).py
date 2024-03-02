"""Faça uma função notas() que receba várias notas e depois mostre a quantidade, a maior, a menor, a média e a situação"""

def titulo(texto):
    print('\033[35m=-=\033[m'*10)
    print(f'\033[32m{texto}\033[m')
    print('\033[35m=-=\033[m'*10)

titulo("Função notas()")

def notas(*lista):
    print("Nº                       Nota            Situação")
    print('=' * 50)
    for i, e in enumerate(lista):
        print(f'{i}.                        {e}', end = '       ')
        if i > 6.0:
            print("Aprovado.")
        else:
            print("Reprovado.")

    relatorio = dict()

    relatorio['Notas Digitadas'] = len(lista)
    relatorio['Maior nota'] = max(lista)
    relatorio['Menor nota'] = min(lista)
    relatorio['Média'] = sum(lista) / len(lista)
    if relatorio['Média'] >= 5 and relatorio['Média'] <= 7:
        relatorio['Situação'] = "Mediana"
    elif relatorio['Média'] > 7:
        relatorio['Situação'] = "Boa"
    else:
        relatorio['Situação'] = "Ruim"
    
    return relatorio

notas(8, 6.8, 9, 4, 5.7)