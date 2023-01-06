stats = {}
goal = []
stats['nome'] = str(input('Nome do jogador: ')).strip().title()
stats['jogos'] = int(input('Nº de partidas jogadas neste mês: '))
for c in range(stats['jogos']):
    goal.append(int(input(f'Gols marcados no jogo {c+1}: ')))
stats['gols'] = goal[:]
stats['total'] = f'{sum(stats["gols"])} gols marcados'
stats['aproveitamento'] = f'{sum(stats["gols"])/stats["jogos"]:.2f} gol por partida.'
print(stats)
print(f'{"[ DADOS ]":+^50}')
for k, v in stats.items():
    print(f'Campo "{k.upper()}" recebe: {v}')
print('+'*50)
for indice, gol in enumerate(stats['gols']):
    print(f'Nº de gols marcados no Jogo {indice+1}: {gol}')
print(f'Um total de {stats["total"]}')  # O ['total'] já inclui a string 'gols marcados'
print('+'*50)
