print('Vamos calcular os 10 primeiros termos de uma PA')
a0 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão que compõe a PA: '))
for c in range(a0, a0 + 10*r, r):
    print('{}'.format(c), end=' ~ ')
print('Pronto!')
