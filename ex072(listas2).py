"""Faça um programa que leia o peso de várias pessoas. Após isso, faça uma listagem de quantas pessoas foram cadastradas, e uma listagem 
dos mais leves e mais pesados."""
print('\033[35m=-=\033[m'*10)
print('\033[32mAnálise de Dados em listas compostas\033[m')
print('\033[35m=-=\033[m'*10)

pessoas = list()
pessoa = list()
maior = None
menor = None
nomeMaior = None
nomeMenor = None

while True: # Leitura de Dados!
    pessoa.append(str(input("Digite seu nome: ")))
    pessoa.append(float(input("Digite seu peso: ")))
    pessoas.append(pessoa[:])
    opc = str(input("\nDeseja continuar? [S/N]: ")).upper()
    while opc not in "SN":
        opc = str(input("Digite novamente: ")).upper()
    match opc:
        case "S":
            continue
        case "N":
            break

for dado in pessoas:
    if dado[1] > maior or dado[1] == None:
        maior = dado[1]
        nomeMaior = dado[0]
    elif dado[1] < menor or dado[1] == None:
        menor = dado[1]
        nomeMenor = dado[0]

print("=-=" * 5)
print(f"Foram analisados os dados de {len(pessoas)} pessoas")
print(f"O maior peso é de {nomeMaior}, com {maior}", end = ' ')
for p in pessoas:
    if p[1] == maior:
        print(p[1], end = " ")
print(f"O menor peso é de {nomeMenor}, {menor}")
for p in pessoas:
    if p[1] == menor:
        print(p[1], end = " ")