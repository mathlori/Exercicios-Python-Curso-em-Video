# Exercício 4: Faça um programa que leia um nome e verifique se há "Silva" nesse nome
name = input('Digite um nome: ')
silva = name.find('Silva')
if silva == -1:
    print('O nome escolhido não tem Silva')
else:
    print('O nome escolhido tem Silva')

