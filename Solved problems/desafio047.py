perg = str(input('Quer saber quais são todos os números pares entre 1 e 50? Sim ou não? ')).strip().upper()
if perg in 'SIM SIMM SIMMM SIMMMM':
    for c in range(2, 51, 2):
        print(c, end=' ')
else:
    print('...')
