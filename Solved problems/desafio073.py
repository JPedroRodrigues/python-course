east_conf = 'Heat', 'Celtics', 'Bucks', 'Sixers', 'Raptors', 'Bulls', 'Nets', 'Hawks', 'Cavs', 'Hornets'
west_conf = 'Suns', 'Grizzles', 'Warriors', 'Mavs', 'Jazz', 'Nuggets', 'Wolves', 'Pelicans', 'Clippers', 'Spurs'
print('''MENU DE OPÇÕES NBA - 2021/2022
[1] - 5 primeiros do Leste
[2] - 5 primeiros do Oeste
[3] - Play-in Leste e Oeste
[4] - Os 20 primeiros times em ordem alfabética
[5] - Posição do Mil e GSW na temporada
[0] - Encerrar o programa''')
while True:
    r = int(input('\nSua opção: '))
    while r not in (0, 1, 2, 3, 4, 5):
        r = int(input('Alternativa Inválida. Sua opção: '))
    if r == 1:
        print('Os 5 primeiros do Leste:')
        for ep, e in enumerate(east_conf[:5]):
            print(f'{ep+1}º - {e}')
    if r == 2:
        print('Os 5 primeiros do Oeste:')
        for w in range(5):
            print(f'{w+1}º - {west_conf[w]}')
    if r == 3:
        print(f'Os times que disputaram o play-in no leste: ', end='')
        for pe in east_conf[-4:]:
            print(pe, end=', ' if pe != east_conf[-1] else '. ')
        print(f'\nTimes que disputaram o play-in no Oeste: ', end='')
        for pw in west_conf[-4:]:
            print(pw, end=', ' if pw != west_conf[-1] else '. ')
    if r == 4:
        print('Lista dos 20 times em ordem alfabética:')
        order = sorted(east_conf+west_conf)
        for c in order:
            print(c)
    if r == 5:
        mil = east_conf.index('Bucks')
        gsw = west_conf.index('Warriors')
        print(f'Posição do Milwaukee Bucks na Conferência leste: {mil+1}º')
        print(f'Posição do Golden State Warriors na Conferência oeste: {gsw+1}º')
    if r == 0:
        break
print('--'*30)
print('Programa encerrado. Tenha um bom dia!')
