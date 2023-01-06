print('Criação de PA com a estrutura "while"')
a0 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c = a0
contador = 1
while contador <= 10:
    print(c, end=' ')
    c += r
    contador += 1
print('\nFIM')
