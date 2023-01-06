for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')

number = 1
par = impar = 0
while number != 0:
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        par += 1
    else:
        impar += 1
print('Quantidades:\nDe números pares: {}\nDe números ímpares: {}'.format(par, impar))
