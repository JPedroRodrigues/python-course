import time
n = int(input('Digite um número: '))
print('Analisando...')
time.sleep(1)
if n % 2 == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar!'.format(n))
