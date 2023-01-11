def aumentar(value=0, percentage=0):
    """
    - > Aumenta determinado número tendo em vista uma determinada porcentagem.
    :param value: Número que se deseja aumentar
    :param percentage: Porcentagem de aumento do valor inserido
    :return: Número aumentado
    """
    v = value * (1 + (percentage/100))
    return v


def dobro(value=0):
    """
    -> Dobro de um número
    :param value: Número que se quer obter o dobro
    :return: Dobro do número inserido
    """
    v = value * 2
    return v


def diminuir(value=0, percentage=0):
    """
    -> Diminui determinado número tendo em vista uma determinada porcentagem.
    :param value: Número que se quer diminuir
    :param percentage: Porcentagem que será decrescida do número digitado
    :return: Número decrescido pela porcentagem escolhida
    """
    v = value * (1 - (percentage/100))
    return v


def metade(value=0):
    """
    -> Metade de um número
    :param value: Número que se quer obter a metade
    :return: Metade do número inserido
    """
    v = value / 2
    return v


def correction(value=0, currency='R$'):
    return f'{currency}{value:.2f}'.replace('.', ',')
