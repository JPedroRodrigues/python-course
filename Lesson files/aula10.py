n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {}'.format(m))
if m >= 6:
    print('Parabéns, você passou!')
else:
    print('Não foi desta vez...')
print('Parabéns' if m >= 6.0 else 'Meu Deus...')
