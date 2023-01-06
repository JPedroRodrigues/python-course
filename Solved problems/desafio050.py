s = 0
contador = 0
print('Me diga 6 números e eu vou somar somente os pares')
for c in range(1, 7):
    n = int(input('{}° número: '.format(c)))
    if n % 2 == 0:
        s += n
        contador += 1
print('A soma dos {} números pares informados é igual a {}.'.format(contador, s))
