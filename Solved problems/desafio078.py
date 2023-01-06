n = [int(input(f'Digite um valor para a posição {c}: ')) for c in range(1, 6)]  # ou list()
cn = 0
print(f'Esses foram os valores digitados: ', end='')
for nu in n:
    cn += 1
    print(f'{nu}', end=', ' if cn < len(n) else '.')
print(f'\nMenor número: {min(n)} --> Posição: ', end='')
for menor, numero in enumerate(n):
    if numero == min(n):
        print(f'{menor+1}', end='ª ')
print(f'\nMaior número: {max(n)} --> Posição: ', end='')
for maior, num in enumerate(n):
    if num == max(n):
        print(f'{maior+1}', end='ª ')
