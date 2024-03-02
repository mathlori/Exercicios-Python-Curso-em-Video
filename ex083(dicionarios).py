'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada 
jogador.'''

print('\033[35m=-=\033[m'*10)
print('\033[32mAprimorando Dicionários\033[m')
print('\033[35m=-=\033[m'*10)

cont = 1
time = {}
while True:

    partidas = []
    jogador = {'nome': str(input('Nome: ')),}
    total = int(input("Partidas jogadas: "))
    for i in range(total):
        partidas.append(int(input(f"Gols na {i + 1} partida: ")))
    jogador['gols por partida'] = partidas
    jogador['total de gols'] = sum(partidas)

    time[f'Jogador {cont}'] = jogador
    cont += 1

    opc = str(input("\nDeseja continuar?: [S/N]")).upper()
    while opc not in "SN":
        opc = str(input("Valor inválido. Desjea continuar? [S/N]: ")).upper()
    
    match opc:
        case "S":
            continue
        case "N":
            break
        case _: 
            print()

while True:
    print("\nNúmero do jogador        Nome        Gols        Total")
    for n,jog in time.items():
        print(f"{n}             {jog['nome']}       {jog['gols por partida']}       {jog['total de gols']}")

    analise = str(input("Deseja fazer a análise de algum jogador?: (999 para parar): "))
    if analise == '999':
        break
    else: 
        for jog in time.values():
                if jog['nome'] == analise:
                    for i, g in enumerate(jog['gols por partida']):
                        print(f"Na {i+1}ª partida fez {g} gols")
                    print("Totalizando:", jog['total de gols'])
            