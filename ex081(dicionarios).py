'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.
'''
print('\033[35m=-=\033[m'*10)
print('\033[32mCadastro de jogador\033[m')
print('\033[35m=-=\033[m'*10)

partidas = []
jogador = {'nome': str(input('Nome: ')),}
total = int(input("Quantas partidas foram jogadas?: "))
for i in range(total):
    partidas.append(int(input(f"Quantos gols na {i + 1} partida?: ")))
jogador['gols por partida'] = partidas
jogador['total de gols'] = sum(partidas)

for i, v in jogador.items():
    print(f'{i} = {v}')