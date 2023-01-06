print('Checagem de multas')
v = float(input('Digite, em km/h, a velocidade do motorista: '))
if v > 80.00:
    print('Este motorista será multado em R${:.2f}'.format((v - 80.00)*7.00))
else:
    print('Não há condições para multas.')
