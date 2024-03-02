"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os 
valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
print('\033[35m=-=\033[m'*10)
print('\033[32mListas compostas e pares e ímpares\033[m')
print('\033[35m=-=\033[m'*10)

nums = []
pares = []
impares = []

for i in range(7): # Lê e separa os valores
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
nums.append(pares)
nums.append(impares)
for i in nums:
    if i % 2 == 0:
        print("\nPares: ", sorted(nums[i]))
    else:
        print("\nÍmpares:", sorted(nums[1]))
