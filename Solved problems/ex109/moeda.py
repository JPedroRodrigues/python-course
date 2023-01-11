def aumentar(value=0, percentage=0, formato=False):
    """
    - > Aumenta determinado número tendo em vista uma determinada porcentagem.
    :param value: Número que se deseja aumentar.
    :param percentage: Porcentagem de aumento do valor inserido.
    :param formato: (Opcional) Formata a apresentação do valor para o modelo monetário brasileiro.
    :return: Número aumentado
    """
    v = value * (1 + (percentage/100))
    return v if formato is False else correction(v)


def dobro(value=0, formato=False):
    """
    -> Dobro de um número.
    :param value: Número que se quer obter o dobro.
    :param formato: (Opcional) Formata a apresentação do valor para o modelo monetário brasileiro.
    :return: Dobro do número inserido.
    """
    v = value * 2
    return v if formato is False else correction(v)


def diminuir(value=0, percentage=0, formato=False):
    """
    -> Diminui determinado número tendo em vista uma determinada porcentagem.
    :param value: Número que se quer diminuir.
    :param percentage: Porcentagem que será decrescida do número digitado.
    :param formato: (Opcional) Formata a apresentação do valor para o modelo monetário brasileiro.
    :return: Número decrescido pela porcentagem escolhida.
    """
    v = value * (1 - (percentage/100))
    return v if not formato else correction(v)


def metade(value=0, formato=False):
    """
    -> Metade de um número
    :param value: Número que se quer obter a metade
    :return: Metade do número inserido
    """
    v = value / 2
    return v if not formato else correction(v)


def correction(value=0.0, currency='R$'):
    """
    -> Formata determinado valor de acordo o modelo de representação monetária brasileiro.
    :param value: Número a ser formatado.
    :param currency: Moeda a ser utilizada. Padrão: Real brasileiro.
    :return: Retorna o valor digitado de acordo com a representação do Real brasileiro.
    """
    return f'{currency}{value:.2f}'.replace('.', ',')
