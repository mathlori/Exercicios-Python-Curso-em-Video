'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o 
usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''

cores = {'Nenhuma': '\033[m', 'Vermelho': '\033[0;30;41m', 'Amarelo': '\033[0;35;43m', 'Verde': '\033[0;30;42m', 'Azul': '\033[0;30;44m'}

def titulo(texto, cor = 'Nenhuma'):
    print(f'{cores[cor]}=-=' * 10)
    print(f'{cores[cor]}{texto}')
    print(f'{cores[cor]}=-=' * 10)

# Função ajuda

def ajuda(com):
    help(com)


# Programa Principal

while True:
    titulo("Interactive Help Python", 'Verde')
    comando = str(input(f"{cores['Nenhuma']} Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        titulo('PROGRAMA FINALIZADO', 'Vermelho')
        break
    else:
        titulo(f"COMANDO {comando}", 'Amarelo')
        ajuda(comando)

