# Exercício 5: Programa que leia um ano e veja se ele é bissexto
print('-='*20)
print('Anos bissextos')
print('-='*20)
ano = int(input('Digite um ano:'))
if ano % 4 == 0:
    print(f'{ano} é um ano bissexto, ou seja, tem 366 dias')
else:
    print(f'{ano} não é um ano bissexto, isso é, tem 365 dias')

