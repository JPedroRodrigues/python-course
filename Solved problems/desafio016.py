import math
print('Parte inteira de um número real')
n = float(input('Digite um número real: '))
print('A parte inteira deste número é {}.'.format(math.trunc(n)))
from math import trunc
n = float(input('Digite um número real: '))
print('A parte inteira é {}.'.format(trunc(n)))

n = float(input('Digite um número: '))
print('A parte inteira de {} é {}.'.format(n, int(n)))
