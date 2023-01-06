import math
print('Desvendando hipotenuzas...')
co = float(input('Digite o valor do cateto oposto do seu triângulo: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenuza de um triângulo de catetos {} e {} é {:.2f}.'.format(co, ca, h))

from math import hypot
co1 = float(input('Valor do cateto oposto: '))
ca2 = float(input('Valor do cato adjacente: '))
print('A hipotenuza deste triângulo é {:.2f}.'.format(hypot(co1, ca2)))

import math
c = float(input('Digite um cateto: '))
c1 = float(input('Digite outro cateto: '))
h1 = math.sqrt(pow(c, 2)+ pow(c1, 2))
print('A hipotenuza de {} e {} é {}.'.format(c, c1, h1))
