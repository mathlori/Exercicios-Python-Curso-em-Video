print('\033[35m=-=\033[m'*10)
print('\033[32mTabuada V3\033[m')
print('\033[35m=-=\033[m'*10)

'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será 
interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('Qual tabuada você quer ver?'))
    r = n
    if n < 0: # Se for negativo, encerra o programa
        print('Programa encerrado.')
        break
    cont = 1
    print(n, end = ' -> ')
    while cont != 10:
        n += r
        print(n, end = ' -> ')
        cont += 1

