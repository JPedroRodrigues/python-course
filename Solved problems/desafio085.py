grupo = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        grupo[0].append(n)
    else:
        grupo[1].append(n)
grupo[0].sort()
grupo[1].sort()
print(f'Números pares digitados: {grupo[0]}')
print(f'Números ímpares digitados: {grupo[1]}')
