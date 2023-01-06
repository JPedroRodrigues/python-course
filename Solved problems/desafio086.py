matriz = [[], [], []]
print(f'{"| Gerador de Matriz 3x3 |":=^50}')
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Número para a posição [{linha}, {coluna}]: ')))
print(f'{"| Matriz Gerada |":=^50}')
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()  # Um print vazio quebra a linha.
