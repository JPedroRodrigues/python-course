print('Identificador de números primos\nDigite números de 1 até 50 para facilitar a visualização')
n = int(input('Digite um número inteiro: '))
contador = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end='')
        contador += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
if contador == 2:
    print('\n\033[mO número {} é considerado primo.\nEle é divisível {} vezes'.format(n, contador))
elif contador == 1:
    print('\n\033[mO número 1 não é primo. Ele é divisível uma única vez.')
else:
    print('\n\033[m{} não é primo. Ele é divisível {} vezes.'.format(n, contador))
