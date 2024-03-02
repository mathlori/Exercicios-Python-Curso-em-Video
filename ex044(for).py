''' Exercício: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do 
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

print('\033[35m=-=\033[m'*10)
print('\033[35m=Analisador Completo\033[m')
print('\033[35m=-=\033[m'*10)
media = 0
cont = 0
maior = 0
for i in range(1, 5): 
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo (M ou F): ')
    media += idade
    if sexo.upper() == 'F' and idade < 20:
        cont += 1
    if sexo.upper() == 'M' and idade > maior:
        maior = idade
        velho = nome
media /= i
print(f'O homem mais velho é {velho} com {maior}, a média de idade é {media}, e existem {cont} mulheres menores de 20 anos')