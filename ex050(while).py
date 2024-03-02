print('\033[35m=-=\033[m'*10)
print('\033[32mProgressão Aritmética Aprimorada\033[m')
print('\033[35m=-=\033[m'*10)

'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele 
disser que quer mostrar 0 termos.'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
print(a1, end = ', ')
while cont != 10:
    a1 += r
    print(a1, end = ', ')
    cont += 1
add = int(input('Quantos termos quer adicionar?: '))
while add != 0:
    for i in range(add):
        a1 += r
        print(a1, end = ', ')
    add = int(input('Quantos termos quer adicionar?: '))
     