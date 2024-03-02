print('\033[35m=-=\033[m'*10)
print('\033[32mSoma dos pares\033[m')
print('\033[35m=-=\033[m'*10)
soma = 0
cont = 0
for i in range(1,7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        print(f'Certo, {numero} vai ser considerado.')
    else:
        print(f'{numero} é ímpar, não irei considerá-lo na soma.')
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'\nA soma dos {cont} numeros pares é {soma}.')

