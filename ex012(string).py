# Exercício 5: Faça um programa que leia uma string e mostre quantas vezes aparece a letra A nela, quando é a primeira
# vez, e quando é a última vez
str = str(input('Digite algo: ')).upper().strip()
stra = str.count('A')
print(f'A letra A aparece {stra} vezes')
print('A primeira letra A aparece na posição {}, e a última na posição {}'.format(str.find('A') + 1, str.rfind('A') + 1))

