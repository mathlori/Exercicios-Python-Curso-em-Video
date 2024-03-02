idade_maior = None
contador_mulheres = 0
contador_18_35 = 0
while True:
  idade = int(input('Digite sua idade (0 para parar): '))
  if idade == 0:
    break
  genero = str(input('Digite seu gênero (M para Masculino, F para Feminino):'))
  while genero != 'M' and genero != 'F':
    genero = input('Valor inválido, digite novamente: ')
  if idade > idade_maior or idade_maior is None:
    idade_maior = idade
  if genero == 'F' and idade >= 18 and idade <= 35:
    contador_18_35 += 1
  contador_mulheres += 1
if contador_mulheres == 0:
    print('')
else:
  print('A pessoa mais velha tem', idade_maior, 'anos.')
  print(f'Dentre as mulheres, {contador_18_35/contador_mulheres * 100} possuem de 18 a 35 anos.')