"""Pegue o exercício anterior e mostre a soma dos valores pares digitados, a soma dos valores da terceira coluna e o maior valor da
 segunda linha"""
print('\033[35m=-=\033[m'*10)
print('\033[32mMatrizes em Python\033[m')
print('\033[35m=-=\033[m'*10)

matriz = [[],[],[]]
for linha in range(len(matriz)): # Leitura dos Valores
    for num in range(3):
        n = int(input(f"Digite um número para [{linha, num}]:"))
        matriz[linha].append(n)

for linha in matriz: # Matriz formatada
    print()
    for i in range(0, len(linha)):
        print(linha[i], end = '     ')

somaPares = 0 # Soma dos elementos pares:
for i in matriz:
    for j in i: 
        if j % 2 == 0:
            somaPares += j

print("\nA soma dos elementos pares da matriz é", somaPares)

soma3 = 0 # Soma dos elementos da terceira coluna
for i in matriz:
    soma3 += i[2]
print("A soma dos valores da terceira coluna é", soma3)

maior = None # Maior da segunda linha
for i in matriz[2]:
    if maior == None or i > maior:
        maior = i
print("O maior valor da segunda linha é: ", maior)