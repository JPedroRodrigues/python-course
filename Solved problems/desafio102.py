def fatorial(number, show=False):
    """
    -> Calcula o fatorial de um número inteiro.
    :param number: Número do qual se obtém o seu fatorial.
    :param show: (Opcional) Mostra a conta realizada.
    :return: Valor fatorial do número inserido no parâmetro.
    """
    fator = 1
    for c in range(number, 0, -1):
        if show:
            print(f'{c}', end=' x ' if c > 1 else ' = ')
        fator *= c
    return fator


# Programa principal
help(fatorial)
# print(fatorial(7, True))
# print(fatorial(9, show=False))
# print(fatorial(3, show=True))
# print(fatorial(5, show=True))
# print(fatorial(8))
