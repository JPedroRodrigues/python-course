def sorteio(lista):
    from random import randint
    while len(lista) != 5:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
    print('Números sorteados:', end=' ')
    print(*lista, sep=', ', end='.')
    print()


def somapar(lista):
    par = []
    for numero in lista:
        if numero % 2 == 0:
            par.append(numero)
    print('Números pares do conjunto:', end=' ')
    print(*par, sep=', ', end='.')
    print(f'\nA soma entre os números pares do conjunto é igual a {sum(par)}.')


# Programa principal
numeros = []
sorteio(numeros)
somapar(numeros)
