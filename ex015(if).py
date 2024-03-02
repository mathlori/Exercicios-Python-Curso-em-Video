# Exercício 15: Escreva um programa que verifica se a velocidade de um carro está dentro do limite. Se não estiver, serão
# cobrados 7 reais a cada quilômetro excedido.
print('-='*20)
print('Radar de velocidade e multa')
print('-='*20)
vel = int(input('A quantos km/h você estava rodando naquele momento? '))
if vel <= 80:
    print('Você estava dentro do permitido.')
else:
    print(f'Você excedeu o limite em {vel - 80}km/h. Por isso, levou uma multa de {(vel - 80)*7} reais. ')

print('-----------------------------')

