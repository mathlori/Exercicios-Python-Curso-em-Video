#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
print('\033[35m=-=\033[m'*10)
print('\033[32mClassificação de triângulos\033[m')
print('\033[35m=-=\033[m'*10)
l1 = int(input('\nQual o valor do primeiro lado?: '))
l2 = int(input('Qual o valor do segundo lado?: '))
l3 = int(input('Qual o valor do terceiro lado?: '))
tri = [l1, l2, l3]
print('\n\033[31;40mAnalisando condição de existência...\033[m')
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Certo! O triângulo existe!')
else:
    print('O triângulo não existe. Utilize outras medidas.')

print('Agora vamos classificá-lo!')
if l1 == l2 == l3:
    print('Esse triângulo é \033[4;36mEquilátero\033[m.')
elif l1 == l2 or l1 == l3 or l1 == l2:
    print('Esse triângluo é \033[4;36mIsósceles\033[m.')
else:
    print('Esse triângulo é \033[4;36mEscaleno\033[m.')
