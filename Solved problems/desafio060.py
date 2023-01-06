print('CÁLCULO DE FATORIAIS')
n = int(input('Digite um número: '))
c = n  # Nosso contador c recebe o número de n
produto = 1
print('Estrutura "WHILE":')
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    produto *= c  # multiplica os valores de c à variável produto, que equivale a 1
    c -= 1  # subtrai 1 dos valores de c (ou n)
print('{}'.format(produto))
print('Estrutura "FOR":')
fatorial = 1
print('{}! = '.format(n), end='')
for f in range(n, 0, -1):
    print('{}'.format(f), end='')
    print(' x ' if f > 1 else ' = ', end='')
    fatorial *= f
    f -= 1
print('{}'.format(fatorial))
