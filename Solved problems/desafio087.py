grupo = [[], [], []]
pares = list()
coluna3 = []
maior = soma3 = 0
print(f'{"| GERADOR DE MATRIZ 3X3 |":=^50}')
for lista in range(3):
    for pos in range(3):
        grupo[lista].append(int(input(f'Número para a posição [{lista+1}, {pos+1}]: ')))
print(f'{"| MATRIZ GERADA |":=^50}')
for matriz in range(3):
    print(f'[{grupo[matriz][0]:^5}][{grupo[matriz][1]:^5}][{grupo[matriz][2]:^5}]')
    coluna3.append(grupo[matriz][2])
    soma3 += grupo[matriz][0]
for lista in grupo:
    for valor in lista:
        if valor % 2 == 0:
            pares.append(valor)
print(f'{"| ESTATÍSTICAS |":=^50}')
print(f'Soma dos números pares, {pares}: {sum(pares)}')
print(f'Soma dos valores da 3ª coluna, {coluna3}: {sum(coluna3)}')
print(f'Maior número da 2ª linha: {max(grupo[1])}')
for coluna in range(0, 3):
    if coluna == 0 or grupo[0][coluna] > maior:
        maior = grupo[0][coluna]
print(f'Maior número da primeira linha: {maior}')
print(f'Soma dos números da primeira coluna: {soma3}')
