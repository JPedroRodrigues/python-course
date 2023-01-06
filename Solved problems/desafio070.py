total = thousand = Ncheapest = Pcheapest = 0
contador = 1
print('\033[1mLOJA JOÃO-PEDRINHO\033[m')
print('=='*10)
while True:
    print(f'{contador}º Produto:')
    name = str(input('Nome: ')).strip().upper()
    price = float(input('Preço: R$'))
    if contador == 1 or price < Pcheapest:  # Esse tipo de simplificação existe e é bem aceitável. Use mais, por favor
        Ncheapest = name
        Pcheapest = price
    if price > 1000:
        thousand += 1
    contador += 1  # Eu só coloquei o meu contador abaixo, pois, neste caso, ele já começa em 1
    total += price
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S]Sim/[N]Não: ')).strip().upper()[0]
    print('==='*10)
    if q in 'N':
        break
print(f'Total a ser pago: R${total:.2f}')
print(f'Quantidade de itens que custam mais de R$1000.00: {thousand}')
print(f'Produto mais barato: {Ncheapest} (R${Pcheapest:.2f})')
