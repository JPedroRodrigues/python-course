numero = str(input('Digite um número inteiro entre 0 e 9999: ')).strip()
sep = ' '.join(numero)
lista = sep.strip().split()
lista.reverse()
casas = '000'
lista.extend(casas)
print('Casa das unidades:', lista[0])
print('Casa das dezenas:', lista[1])
print('Casa das centenas:', lista[2])
print('Casa dos milhares:', lista[3])

num = int(input('Informe um número inteiro: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(m))
