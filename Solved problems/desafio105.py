def notas(*n, sit=False):
    """
    -> Realiza análise de um conjunto de notas escolares.
    :param n: Uma ou mais notas inseridas.
    :param sit: Parâmetro opcional que adiciona uma análise
    avaliativa, tendo em vista a média das notas do grupo
    :return: Retorna um dicionário contendo os resultados da análise.
    """
    ficha = dict()
    ficha['maior nota'] = max(n)
    ficha['menor nota'] = min(n)
    ficha['nº de notas'] = len(n)
    ficha['média'] = f'{sum(n)/len(n):.2f}'
    if sit:
        if sum(n)/len(n) >= 7:
            ficha['situação'] = 'Boa'
        elif 5 <= sum(n)/len(n) < 7:
            ficha['situação'] = 'Razoável'
        else:
            ficha['situação'] = 'Ruim'
    return ficha


# Programa Principal
help(notas)
boletim = notas(3, 10, 9, 8.75, 10, 9.5, 6.5, sit=True)
for k, v in boletim.items():
    print(f'{k.capitalize()}: {v}')
