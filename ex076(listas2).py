"""Faça um programa que leia uma quantidade de jogos que serão feitos na megasena, e sorteie 6 números aleatórios para cada jogo."""
print('\033[35m=-=\033[m'*10)
print('\033[32mMegasena\033[m')
print('\033[35m=-=\033[m'*10)

from random import randint

jogos = int(input("Quantos jogos serão feitos: "))
palpites = []
for i in range(jogos):
    palpites.append([])

for jogo in palpites: # Percorre a lista composta
    for numero in range(6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)

for i, j in enumerate(palpites):
    print(f"Jogo {i+1}:", sorted(j))