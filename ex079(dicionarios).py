'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
 No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

print('\033[35m=-=\033[m'*10)
print('\033[32mJogo dos dados\033[m')
print('\033[35m=-=\033[m'*10)

from random import randint
from operator import itemgetter # Analisa dicionários através de um critério 0 (chave) ou 1 (valor)

jogadores = dict()

jogadores['J1'] = randint(1, 6)
jogadores['J2'] = randint(1, 6)
jogadores['J3'] = randint(1, 6)
jogadores['J4'] = randint(1, 6)

for i, v in jogadores.items():
    print(f'{i} tirou {v}')

ranking = sorted(jogadores.items(), key = itemgetter(1))

for i,v in enumerate(ranking):
    print(i,'º', '=', v, 'pontos')