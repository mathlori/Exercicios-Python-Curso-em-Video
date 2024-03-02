"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No 
final, mostre uma listagem de preços, organizando os dados em forma tabular."""

print('\033[35m=-=\033[m'*10)
print('\033[32mLista de Preços\033[m')
print('\033[35m=-=\033[m'*10)

precos = ("Lápis", 1.50, "Borracha", 2.0, "Caneta", 3.00, "Caderno", 10.00, "Estojo", 12, "Mochila", 100)

print(""" 
------------------------------------------------------------
                    LISTA DE PREÇOS
------------------------------------------------------------
""")
for i in range(0, len(precos), 2):
    print(f'{precos[i]:.<30} R$ {precos[i+1]}')
print("------------------------------------------------------------")   
