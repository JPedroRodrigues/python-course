cor = {'azul': '\033[1;34m', 'l': '\033[m'}
print('{}{:-^52}{}'.format(cor['azul'], ' TABUADA ', cor['l']))
n = int(input('Digite um número inteiro e eu lhe direi sua tabuada: '))
for c in range(1, 11):
    print('{}{}{} x {:2} = {}'.format(cor['azul'], n, cor['l'], c, n*c))
