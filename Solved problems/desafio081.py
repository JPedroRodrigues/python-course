n = []
while True:
    n.append(int(input('Digite um número: ')))
    r = ' '
    while r not in 'sn':
        r = str(input('Continuar? [s]Sim/[n]Não: ')).strip().lower()[0]
    if r == 'n':
        break
print(f'Nº de valores digitados: {len(n)}')
n.sort(reverse=True)
print(f'Números em ordem decrescente:', end=' ')
print(*n, sep=', ', end='.')
if 5 not in n:
    print('\nO número 5 não está inserido nos valores digitados.')
else:
    print('\nO número 5 foi digitado e se encontra na posição: ', end='')
    for p, c in enumerate(n):
        if c == 5:
            print(f'{p+1}', end='ª ')
