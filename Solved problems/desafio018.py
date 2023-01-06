from math import radians, sin, cos, tan

a = float(input('Digite, em graus, o valor de um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
h = tan(radians(a))
print('Seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(s, c, h))
