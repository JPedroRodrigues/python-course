team = list()
points = []
player = {}
while True:
    player.clear()
    player['name'] = str(input('Nome do jogador: ')).strip().title()
    player['matches'] = int(input('Nº de partidas jogadas: '))
    for c in range(player['matches']):
        points.append(int(input(f'Pontos marcados no {c+1}º jogo: ')))
    player['points'] = points[:]
    points.clear()
    player['ppg'] = sum(player['points'])/player['matches']
    team.append(player.copy())
    while True:
        opc = str(input('Adicionar mais um jogador? (Sim/Não): ')).strip().lower()
        if opc not in 'simnãonao' or opc == '':
            print('\033[1;31mERRO!\033[m Digite somente "sim" ou "não".')
        else:
            break
    if opc in 'nãonao':
        print(f'{"| Tabela de Dados |":-^50}')
        print(f'{"Position":<10}{"Name":<30}{"PPG":>10}')
        print('-'*50)
        for pos, info in enumerate(team):
            print(f'{pos:<10}{info["name"]:<30}{info["ppg"]:>10.2f}')
        print('-'*50)
        break
    print('-'*50)
while True:
    print('Para encerrar este programa, digite 999.')
    detail = int(input('Informe a posição do jogador para obter mais detalhes: '))
    if detail in range(len(team)):
        print('='*50)
        print(f'Dados sobre {team[detail]["name"]}:')
        print('-'*50)
        print(f'Nº de jogos disputados: {team[detail]["matches"]}')
        for game, points in enumerate(team[detail]['points']):
            print(f'Pontos marcados no jogo {game+1}: {points}')
        print('-'*50)
        print(f'Pontos por jogo: {team[detail]["ppg"]:.2f}')
        print(f'Total de pontos marcados nestes {team[detail]["matches"]} jogos: {sum(team[detail]["points"])}')
        print('='*50)
    elif detail == 999:
        print(f'{"| Programa Encerrado |":-^50}')
        break
    else:
        print(f'O número {detail} não está presente na lista "Position". Digite corretamente.')
        print('-'*50)
print('Volte sempre!')
