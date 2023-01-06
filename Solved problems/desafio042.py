print('ANÁLISE SOBRE TRIÂNGULOS')
x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))
if x == y != z or x == z != y or y == z != x:
    tipo = 'isósceles'
elif x == y == z:
    tipo = 'equilátero'
else:
    tipo = 'escaleno'
if y - z < x < y + z and x - z < y < x + z and x - y < z < x + y:
    print('As medidas {}, {} e {} podem formar um triângulo do tipo {}.'.format(x, y, z, tipo))
else:
    print('As medidas {}, {} e {} não formam um triângulo.'.format(x, y, z))
