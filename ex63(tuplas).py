"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

print('\033[35m=-=\033[m'*10)
print('\033[32Análise de dados em tupla\033[m')
print('\033[35m=-=\033[m'*10)

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro:"))
num3 = int(input("Mais um: "))
num4 = int(input("O último: "))

valores = (num1, num2, num3, num4)
cont9 = 0
pos3 = 0
apareceu3 = 1

for i in valores:
    if i == 9:
        cont9 += 1
    if i == 3 and apareceu3 == 1:
        pos3 = valores.index(3)
        apareceu3 += 1

print(f"O valor 9 apareceu {cont9} vezes")
if apareceu3 == 1:
    print("Não há nenhum número 3 na tupla.")
else:
    print("A posição do primeiro 3 foi", valores.index(3))
print("Os números pares foram: ", end = " ")
for i in valores:
    if i % 2 == 0:
        print(i, end = " ")