def teste(b):
    """
    -> Explicita as diferenças entre o escopo global e local.
    :param b: Recebe uma variável que já possua um valor numérico.
    :return: sem retorno
    """
    global a
    a = 8
    b += 4
    c = 2
    print(f'"a" dentro vale {a}')
    print(f'"b" dentro vale {b}')
    print(f'"c" dentro vale {c}')


# Programa Principal
a = 5
print(f'"a" fora antes da função vale {a}')
teste(a)
print(f'"a" fora depois da função vale {a}')


def somar(x=0, y=0, z=0):
    """
    -> Realiza o cálculo de adição entre três números.
    :param x: Primeiro número
    :param y: Segundo número
    :param z: Terceiro número
    :return: Retorna a variável s = x + y + z
    """
    s = x + y + z
    return s


r1 = somar(1, 2, 3)
r2 = somar(3, 4, 5)
r3 = somar(7, 3, 5)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


numero = int(input('Digite um número'))
print(f'Este número é par?')
if par(numero) is True:
    print('É par!')
else:
    print('É ímpar!')
