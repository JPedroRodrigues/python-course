numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    r = str(input('Coninuar? [S]sim/[N]não: ')).strip().upper()
    if r not in 'SIM' or r == '':
        print('Programa encerrado.')
        break
for p in numeros:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print(f'Lista completa: {numeros}')
print(f'Números pares da lista: {pares}')
print(f'Números ímpares da lista: {impares}')
