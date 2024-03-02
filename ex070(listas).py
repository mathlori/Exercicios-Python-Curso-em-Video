"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os 
valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

print('\033[35m=-=\033[m'*10)
print('\033[32mDividindo valores em mais de uma lista\033[m')
print('\033[35m=-=\033[m'*10)

nums = list()

while True:
    num = int(input("Digite um número: "))
    nums.append(num)

    opc = input("Deseja continuar? [S/N]: ").upper()
    while opc not in "SN":
        opc = input("Deseja continuar? [S/N]: ").upper()
    match opc:
        case "S":
            continue
        case "N":
            nums.sort(reverse= True)
            break

pares = list()
impares = list()

for numero in nums:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"""
Lista padrão: {nums}
Pares: {pares}
Ímpares: {impares}
""")