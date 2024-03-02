"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
 ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

print('\033[35m=-=\033[m'*10)
print('\033[32mValores únicos em listas\033[m')
print('\033[35m=-=\033[m'*10)

valores = []
while True:
    print(valores)
    valor = int(input("Digite um valor: "))
    if valor not in valores:
        valores.append(valor)
    opc = input("Deseja continuar? [S/N]")
    while opc.upper() not in ("SN"):
        opc = input("Digite novamente. Deseja continuar?: ")
    match opc:
        case "S":
            continue
        case "N":
            valores.sort()
            print(valores)
            break