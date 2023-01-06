conjunto = []
maior = 0
for c in range(1, 6):
    n = int(input(f'Digite o {c}º número da lista: '))
    if c == 1 or n > maior:
        maior = n
        conjunto.append(n)
        print(f'Número {n} inserido na última posição.')
    else:
        position = 0
        while position < len(conjunto):
            if n < conjunto[position]:
                conjunto.insert(position, n)
                print(f'Número {n} inserido na posição {position}.')
                break
            position += 1
print('Lista final: ', end='')
print(*conjunto, sep=', ', end='.')
