compasso = input('')
compasso = compasso.replace('/', ' ').strip().split()
contador = 0
for i in range (0, len(compasso)):
  tempo_compasso = 0
  if compasso[i].isalpha() == False:
    contador = ''
    break
  if compasso[i].count('W') != 0:
    tempo_compasso += 1 * compasso[i].count('W')
  if compasso[i].count('H') != 0:
    tempo_compasso+= 1/2 * compasso[i].count('H')
  if compasso[i].count('Q') != 0:
    tempo_compasso += 1/4 * compasso[i].count('Q')
  if compasso[i].count('E') != 0:
    tempo_compasso += 1/8 * compasso[i].count('E')
  if compasso[i].count('S') != 0:
    tempo_compasso += 1/16 * compasso[i].count('S')
  if compasso[i].count('T') != 0:
    tempo_compasso += 1/32 * compasso[i].count('T')
  if compasso[i].count('X') != 0:
    tempo_compasso += 1/64 * compasso[i].count('X')
  if tempo_compasso == 1:
     contador += 1
print(contador)