prod = 'Régua 30cm', 10.25, 'Lápis', 2, 'Caneta', 2.25, 'Caneta 4 cores', 3.50,\
       'Borracha', 2, 'Estojo', 40, 'Mochila', 120, 'Kit Lápis de Cor', 75.67, 'Compasso', 4.99, 'Esquadro', 25.99
name = prod[::2]
price = prod[1::2]
print(f'\n{"LOJAS JOÃO PEDRINHO":^53}')
print('--'*30)
for item in range(len(name)):
    print(f'{name[item]:.<50} R${price[item]:>7.2f}')
print('--'*30)
