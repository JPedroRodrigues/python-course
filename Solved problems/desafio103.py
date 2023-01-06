def ficha(nome='<desconhecido>', gols=0):
    """
    -> Informa, em forma de frase, o nome de um atleta e o número de gols marcados por ele.
    :param nome: Nome do atleta
    :param gols: Gols marcados
    :return: Sem retorno
    """
    print(f'O jogador {nome} fez {gols} gol(s) neste campeonato.')


print(f'{"| Leitura de dados de atletas futebolísticos |":=^60}')
n = str(input('Nome do jogador: ')).title().strip()
g = str(input('Gols marcados no campeonato: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
