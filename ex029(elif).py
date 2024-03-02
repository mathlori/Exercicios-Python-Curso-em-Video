from math import pow
#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
# Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

print('\033[35m=-=\033[m'*10)
print('\033[32mCálculo de IMC\033[m')
print('\033[35m=-=\033[m'*10)
h = float(input('\nQual a altura da pessoa (em metros)?: '))
m = float(input('Qual a massa da pessoa? (em kg): '))
imc = m/pow(h,2)
print('Lembre-se: – IMC abaixo de 18,5: Abaixo do Peso\n– Entre 18,5 e 25: Peso Ideal\n– 25 até 30: Sobrepeso',end= '')
print('\n– 30 até 40: Obesidade\n– Acima de 40: Obesidade Mórbida')

if imc < 18.5:
    print(f'\nSeu IMC é de {imc:.2f}, portanto, você está \033[4;31mabaixo do peso\033[m.')
elif 18.5 <= imc < 25:
    print(f'\nSeu IMC é de {imc:.2f}, portanto, você está no \033[4;31mpeso ideal\033[m.')
elif 25 <= imc < 30:
    print(f'\nSeu IMC é de {imc:.2f}, portanto, você está em \033[4;31msobrepeso\033[m.')
elif 30 <= imc < 40:
    print(f'\nSeu IMC é de {imc:.2f}, portanto, você está com \033[4;31mobesidade\033[m.')
else:
    print(f'\nSeu IMC é de {imc:.2f}, portanto você está com \033[4;31mobesidade mórbida\033[m.')

