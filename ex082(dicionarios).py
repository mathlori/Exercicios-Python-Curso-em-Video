'''Crie um programa que leia nome, sexo e idade de várias pessoas, armazenando os dados de cada pessoa em um dicionário. No final, mostrando:
A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
'''

print('\033[35m=-=\033[m'*10)
print('\033[32mDicionários e listas\033[m')
print('\033[35m=-=\033[m'*10)

pessoas = {}
cont = 1

while True:
   pessoa = [] 
   nome = str(input("Nome: "))
   if nome == '-1':
      break
   sexo = str(input("Sexo: [M/F]")).upper()
   while sexo not in "MF":
      sexo = str(input("Sexo: "))
   idade = int(input("Idade: "))
   print('')
   pessoa.append(nome)
   pessoa.append(sexo)
   pessoa.append(idade)
   pessoas[f'pessoa {cont}'] = pessoa
   cont += 1





print(f"\nPessoas cadastradas: {len(pessoas)}")

soma = 0
for i in pessoas.values():
   soma += i[2]
media = soma / len(pessoas)
print(f"A média de idade é {media}")

mulheres = list()
for i in pessoas.values():
   if i[1] == 'F':
      mulheres.append(i)
print("Mulheres", mulheres)

veios = []
for i in pessoas.values():
   if i[2] > media:
      veios.append(i)
print("Pessoas com idade acima da média: ", veios)
