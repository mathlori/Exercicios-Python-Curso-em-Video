# Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
print('\033[35m=-=\033[m'*10)
print('\033[32mSoma de pares múltiplos de 3.\033[m')
print('\033[35m=-=\033[m'*10)
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'A soma dos valores é {soma} e são, ao todo, {cont} números.')

