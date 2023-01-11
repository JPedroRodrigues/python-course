def aumentar(value, percentage):
    """
    - > Aumenta determinado número tendo em vista uma determinada porcentagem.
    :param value: Número que se deseja aumentar
    :param percentage: Porcentagem de aumento do valor inserido
    :return: Número aumentado
    """
    v = value * (1 + (percentage/100))
    return v


def dobro(value):
    """
    -> Dobro de um número
    :param value: Número que se quer obter o dobro
    :return: Dobro do número inserido
    """
    v = value * 2
    return v


def diminuir(value, percentage):
    """
    -> Diminui determinado número tendo em vista uma determinada porcentagem.
    :param value: Número que se quer diminuir
    :param percentage: Porcentagem que será decrescida do número digitado
    :return: Número decrescido pela porcentagem escolhida
    """
    v = value * (1 - (percentage/100))
    return v


def metade(value):
    """
    -> Metade de um número
    :param value: Número que se quer obter a metade
    :return: Metade do número inserido
    """
    v = value / 2
    return v
