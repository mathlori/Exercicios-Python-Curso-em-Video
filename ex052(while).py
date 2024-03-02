print('\033[35m=-=\033[m'*10)
print('\033[32mTratando vários valores\033[m')
print('\033[35m=-=\033[m'*10)

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
 condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = None
cont = 0
soma = 0
parar = 1
while parar != 0:
    n = int(input('Digite um número: '))
    if n == 999:
        parar = 0
    else:
        soma += n
        cont += 1
print(f'Foram digitados {cont} números. A soma entre todos eles é {soma} ')