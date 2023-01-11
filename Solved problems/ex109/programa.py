from ex109 import moeda
n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.correction(n)} é {moeda.metade(n, formato=True)}')
print(f'O dobro de {moeda.correction(n)} é {moeda.dobro(n, True)}')
print(f'Acréscimo de 15% de {moeda.correction(n)} resulta em {moeda.aumentar(n, 15, True)}')
print(f'Decréscimo de 30% de {moeda.correction(n)} resulta em {moeda.diminuir(n, 30, True)}')
