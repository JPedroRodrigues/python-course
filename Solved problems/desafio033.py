from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
print('Analisando...')
sleep(1)
print('Análise concluída com sucesso!')
sleep(1)
if n1 < n2 and n1 < n3:
    print('Menor número: {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Menor número: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Menor número: {}'.format(n3))
if n1 > n2 and n1 > n3:
    print('Maior número: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Maior número: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Maior número: {}'.format(n3))

d = int(input('Digite outro número: '))
e = int(input('Outro: '))
f = int(input('E outro: '))
menor = d
if e < d and e < f:
    menor = e
if f < d and f < e:
    menor = f
maior = d
if e > d and e > f:
    maior = e
if f > d and f > e:
    maior = f
print('Maior número: {}\nMenor número: {}'.format(maior, menor))
