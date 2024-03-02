"""Crie um programa que leia uma matriz 3x3 e mostre ela com a formatação correta."""
print('\033[35m=-=\033[m'*10)
print('\033[32mMatrizes em Python\033[m')
print('\033[35m=-=\033[m'*10)

matriz = [[],[],[]]
for linha in range(len(matriz)): # Leitura dos Valores
    for num in range(3):
        n = int(input(f"Digite um número para [{linha, num}]:"))
        matriz[linha].append(n)

for linha in matriz:
    print()
    for i in range(0, len(linha)):
        print(linha[i], end = '     ')