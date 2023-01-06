import math
n = int(input('Digite um número inteiro: '))
r1 = math.sqrt(n)
print('A raiz de {} é {}.'.format(n, math.floor(r1)))

#Se eu quiser especificar a funcionalidade da biblioteca:

from math import sqrt, floor
n = int(input('Digite um número inteiro: '))
r2 = sqrt(n)
print('A raiz de {} é {:.2f}.'.format(n, floor(r2)))
