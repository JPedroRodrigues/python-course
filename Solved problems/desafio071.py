print('\033[1m{:^29}\033[m'.format('Banco JP'))
print('=='*15)
'''while True:
    value = int(input('Valor do saque: R$'))
    c = value // 50  # Quantos "50" cabe no número
    rc = value % 50  # Resto da divisão por 50. Caso não haja, o resto é igual ao número digitado
    v = rc // 20  # Quantos "20" cabe no resto da divisão por 50(rc)
    rv = rc % 20
    d = rv // 10  # Quantos "10" cabe no resto da divisão por 20(rv)
    rd = rv % 10
    u = rd // 1  # Quantos "1" cabe no resto da divisão por 10(rd)
    ru = rd % 1  # Resto de "1" sempre resultará em 0
    if c > 0:
        print(f'Total de cédulas de R$50: {c}')
    if v > 0:
        print(f'Total de cédulas de R$20: {v}')
    if d > 0:
        print(f'Total de cédulas de R$10: {d}')
    if u > 0:
        print(f'Total de cédulas de R$1: {u}')
    print('=='*15)
    if ru == 0:
        break
print('Foi um prazer tê-lo por aqui. Volte sempre!')'''
quantia = int(input('Valor do saque: '))
cedula = 200
n_cedula = 0
while True:
    if quantia >= cedula:
        quantia -= cedula
        n_cedula += 1
    else:
        if n_cedula > 0:
            print(f'Cédulas de R${cedula}: {n_cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        n_cedula = 0
        if quantia == 0:
            break
print('=='*15)
print('Foi um prazer tê-lo por aqui. Volte sempre!')
