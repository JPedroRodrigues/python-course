from random import randint
r = str(input('Tá a fim de ver  uma sequência de 5 números aleatórios? Sim ou não?')).strip().capitalize()
st = 'Sim' in r
if st is True:
    print(f'"{r}"? Lá vai então...')
    contador = 0
    tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
    print('Sequência aleatória de números: ', end='')
    for c in tupla:
        print(c, end=', ' if contador < 4 else '.')
        contador += 1
    print(f'\nO menor: {min(tupla)}')
    print(f'O maior: {max(tupla)}')
else:
    print(f'"{r}"? Beleza então...')
