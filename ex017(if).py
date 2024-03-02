# Exercício 4: Crie um programa que leia uma distância para uma viagem. Se for até 200km, o valor da passagem será de 50
# centavos por km. Se for mais longo do que isso, custará 45 centavos.
print('-='*20)
print('Análise de preços de viagem a partir de distâncias')
print('-='*20)
distancia = int(input('Qual a distância da sua viagem? '))
if distancia < 200:
    print(f'O valor da passagem será de {distancia * 0.5}')
else: print(f'O valor da passagem será de {distancia * 0.45}')

