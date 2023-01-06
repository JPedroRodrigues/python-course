def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


def soma(*numero):
    s = 0
    for n in numero:
        s += n
    print(f'A soma entre os valores {numero} é igual a {s}.')


soma(2, 4, 6, 8)
conjunto = [1, 2, 4, 5]
dobra(conjunto)
print(conjunto)
