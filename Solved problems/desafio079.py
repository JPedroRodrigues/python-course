n = list()
cont = 0
while True:
    n.append(int(input('Digite um número: ')))
    if n.count(n[-1]) == 2:
        print(f'Este número já foi adicionado.')
        del n[-1]
    else:
        print('Novo valor contabilizado...')
    r = ' '
    while r not in 'SN':
        r = str(input('Continuar? [S]sim/[N]não: ')).strip().upper()[0]
    if r in 'N':
        break
n.sort()
print('Lista gerada: ', end='')
for c in n:
    cont += 1
    print(f'{c}', end=', ' if cont < len(n) else '.')
