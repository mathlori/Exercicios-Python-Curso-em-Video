# Exercício 3: Faça um programa que leia o nome de uma cidade e verifique se nela tem o nome "Santo"
cidade = input('Digite o nome de uma cidade: ')
santo = cidade.find('Santo')
if santo == -1:
    print('Sua cidade não tem Santo no nome')
else:
    print('Sua cidade tem Santo no nome')

