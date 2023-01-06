print('Sequência de Fibonacci')
n = int(input('Digite no número de termos que você quer visualizar nesta sequência: '))
contador = 2
t1 = 0
t2 = 1
print('{} {}'.format(t1, t2), end=' ')
while contador < n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' ')
    contador += 1
    t1 = t2
    t2 = t3
print('\nEstes são os {} primeiros termos da sequência!'.format(contador))
