from random import randint
from time import sleep
from operator import itemgetter  # essa lib nos ajuda a organizar os values do dicionário
dados = {}
ranking = dict()  # Outra forma de organizar
cont = 1
print('4 jogadores sortearam um número de um dado. O maior número sorteado declara o vencedor.')
print('Vamos ver que vence?')
sleep(4)
print(f'{"| JOGADAS |":=^30}')
for c in range(1, 5):
    sleep(1)
    dados[f'Jogador {c}'] = randint(1, 6)
    print(f'Jogador {c} sorteou {dados[f"Jogador {c}"]}')
sleep(1)
print(f'{"| RANKING |":=^30}')
for k, v in sorted(dados.items(), key=lambda x: x[1], reverse=True):
    sleep(1)
    print(f'{cont}º - {k} com nº {v}')
    cont += 1
# O valor do itemgetter ser 1 nos diz que os valores serão analisados, e não as chaves
# Ainda que nos dicionários existam índices literais, posso facilmente afirmar que 0 se refere às chaves e 1, aos values
# , uma vez que o método ".items()" cria tuplas para cada conjunto key-value e as coloca em uma lista
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for indice, numero in enumerate(ranking):
    print(f'{indice+1}º lugar - {numero[0]} com o número {numero[1]}')
for jogador, numero in ranking:
    print(f'{jogador} tirou {numero}')
# Posso ou não usar o enumerate(), mesmo declarando 2 variáveis. O enumerate() me traria a vantagem de obter posições
