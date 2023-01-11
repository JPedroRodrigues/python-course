from ex108 import moeda
n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.correction(n)} é {moeda.correction(moeda.metade(n))}')
print(f'O dobro de {moeda.correction(n)} é {moeda.correction(moeda.dobro(n))}')
print(f'Acréscimo de 15% de {moeda.correction(n)} resulta em {moeda.correction(moeda.aumentar(n, 15))}')
print(f'Decréscimo de 30% de {moeda.correction(n)} resulta em {moeda.correction(moeda.diminuir(n, 30))}')
