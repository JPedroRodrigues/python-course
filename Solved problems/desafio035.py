print('Vamos construir um triângulo!')
a = float(input('Comprimento do primeiro lado: '))
b = float(input('Comprimento do segundo lado: '))
c = float(input('Comprimento do terceiro lado: '))
if a - b < c < a + b and b - c < a < b + c and a - c < b < a + c:
    print('É possível montar um triângulo com os lados {}, {} e {}.'.format(a, b, c))
else:
    print('Não é possível criar um triângulo com essas medidas: {}, {} e {}.'.format(a, b, c))
