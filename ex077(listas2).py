"""Faça um programa que leia a nota de vários alunos e coloque a média no final. Dê a opção de mostrar as notas de cada aluno
 individualmente no fim"""
print('\033[35m=-=\033[m'*10)
print('\033[32mBoletim com listas compostas\033[m')
print('\033[35m=-=\033[m'*10)


alunos = list()
cont = 1
while True: 
    nome = str(input(f"Nome do {cont}º aluno: ")) # Preenchimento dos dados
    nota1 = float(input("   Nota 1: "))
    nota2 = float(input("   Nota 2: "))

    alunos.append([nome, nota1, nota2]) # Cadastro dos dados

    opc = str(input("Deseja continuar? [S/N]: ")).upper() # Opção para continuar
    while opc not in "SN": 
        opc = str(input("Valor inválido. Deseja continuar? [S/N]: "))
    match opc:
        case "S":
            cont += 1
            continue
        case "N": 
            break

print("=-="*7)
print("No.      Aluno       Média")
print("=-="*7)
for i, aluno in enumerate(alunos):
    print(f"{i}     {aluno[0]}       {(aluno[1] + aluno[2])/2}")

notaAluno = str(input("Deseja ver a nota de algum aluno? [Use 999 se não quiser]: "))

nomes = []
for aluno in alunos:
    nomes.append(aluno[0]) # Cria uma lista com nomes para verificar se o aluno digitado está cadastrado.

while notaAluno not in nomes:
    notaAluno = str(input("Valor inválido ou aluno não cadastrado. Deseja ver a nota de algum aluno? [Use 999 se não quiser]: "))

if notaAluno == "999":
    print("Certo! Programa encerrado.")
else:
    for aluno in alunos:
        if notaAluno == aluno[0]:
            print(f"As notas de {aluno[0]} foram {aluno[1]} e {aluno[2]} ")
