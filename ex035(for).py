# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

print('\033[35m=-=\033[m'*10)
print('\033[32mTabuada v2\033[m')
print('\033[35m=-=\033[m'*10)
numero = int(input('\nQual número você quer fazer a tabuada?: '))
soma = 0
for i in range (1,11):
    print(f'{numero} x {i} = {numero * i}')


