from ex107 import moeda
n = float(input('Digite um preço: R$'))
print(f'A metade de R${n:.2f} é {moeda.metade(n)}')
print(f'O dobro de R${n:.2f} é {moeda.dobro(n)}')
print(f'Acréscimo de 15% de R${n:.2f} resulta em {moeda.aumentar(n, 15)}')
print(f'Decréscimo de 30% de R${n:.2f} resulta em {moeda.diminuir(n, 30)}')
