print('Conversão reais em dólar')
d = float(input('Quantos reais você possui em sua carteira? R$'))
print('Considerando que o dólar custa, atualmente, R$4.77, você pode comprar {:.2f} dólares.'.format(d/4.77))
print('Outras cotações: \nEuro: {:.2f}; Libra: {:.2f}'.format(d/5.12, d/5.97))
print('Iene: {:.2f}; Won Coreano: {:.2f}'.format(d*27.41, d*262.10))
