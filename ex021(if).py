# Exercício 8: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = int(input('Digite o valor de um dos lados: '))
r2 = int(input('Digite o valor de outro dos lados: '))
r3 = int(input('Digite o valor do último lado (é um triângulo kkkkk): '))
tri = [r1, r2, r3]
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Esses três seguimentos formam um triângulo')
else:
    print('Esses três seguimentos não formam um triângulo')