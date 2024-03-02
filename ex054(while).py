print('\033[35m=-=\033[m'*10)
print('\033[32mVários números com Flag\033[m')
print('\033[35m=-=\033[m'*10)

'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

cont = 0
soma = 0

while True: 
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Foram digitados {cont} números, e a soma de todos eles é {soma}.')