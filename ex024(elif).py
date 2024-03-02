# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma
# mensagem:
# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais
print('\033[35m=-=\033[m'*10)
print('\033[32mComparador de números\033[m')
print('\033[35m=-=\033[m'*10)
n1 = int(input('\n Digite o primeiro número: '))
n2 = int(input('\n Digite o segundo número: '))

if n1 > n2:
    print('\n➜ O \033[31mprimeiro valor\033[m é \033[4;34mmaior\033[m.')
elif n2 > n1:
    print('\n➜ O \033[31msegundo valor é\033[m \033[4;34mmaior\033[m.')
else:
    print('\n➜ Não há diferença, ambos são \033[4;33miguais\033[m.')