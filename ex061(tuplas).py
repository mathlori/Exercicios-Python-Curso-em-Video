"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

print('\033[35m=-=\033[m'*10)
print('\033[32mTimes do Brasileirão\033[m')
print('\033[35m=-=\033[m'*10)

times = ("Botafogo", "Palmeiras", "Atlético MG", "Grêmio", "Flamengo", "Fluminense", "Athletico PR", "São Paulo", "Fortaleza", "Cruzeiro", "Bragantino", "Santos", "Internacional", "Cuiabá", "Bahia", "Corinthians", "Goiás", "América-MG", "Vasco da Gama", "Coritiba")

print("Os primeiros times são: ", times[0:5])
print("Os times que estão na zona de rebaixamento: ", times[16:])



print("Os times em ordem alfabética são:", sorted(times))
posPalmeiras = times.index("Palmeiras")
print(f"A posição do Palmeiras é a {posPalmeiras + 1}ª")