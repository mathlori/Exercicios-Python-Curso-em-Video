""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o 
menor valor digitado e as suas respectivas posições na lista."""

print('\033[35m=-=\033[m'*10)
print('\033[32mMaior e menor valor em listas\033[m')
print('\033[35m=-=\033[m'*10)

nums = list()

for i in range(1, 6):
    n = int(input(f"Digite o valor do {i}º número: "))
    nums.append(n)

menor = None
maior = None
for i in range(0, len(nums)):
    if menor == None or nums[i] < menor:
        menor = nums [i]
    if maior == None or nums[i] > maior:
        maior = nums[i]

print(f"O maior elemento da lista é {maior}")
print(f"O menor elemento da lista é {menor}")