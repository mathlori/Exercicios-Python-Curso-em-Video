"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:                                                                                                                                               
    A) Quantos números foram digitados.                                                                                                                    
    B) A lista de valores, ordenada de forma decrescente.                                                                                          
    C) Se o valor 5 foi digitado e está ou não na lista."""                                                                 

print('\033[35m=-=\033[m'*10)
print('\033[32mExtraindo dados de uma lista\033[m')
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

print(f"""
Números digitados: {len(nums)}
Números ordenados inversamente: {nums}
""")

if 5 in nums:
    print(f"5 está na lista, na posição {nums.index(5)}")
else:
    print("O número 5 não se encontra na lista.")