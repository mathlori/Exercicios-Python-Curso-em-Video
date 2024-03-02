"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
 (sem usar o sort()). No final, mostre a lista ordenada na tela."""

print('\033[35m=-=\033[m'*10)
print('\033[32mOrdenação sem a função sort\033[m')
print('\033[35m=-=\033[m'*10)

v = []
for i in range(0,5):
    valor = int(input("Digite um número: "))
    if len(v) == 0 or valor > v[len(v)-1]:
        print("Adicionado ao final da lista")
        v.append(valor)
    else:
        for pos in range(0, len(v)):
            if valor <= v[pos]:
                print("Valor inserido na posição", pos)
                v.insert(pos, valor)
print("Os valores, em ordem, são:", v)