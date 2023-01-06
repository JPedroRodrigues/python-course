print('ANÁLISE DE AUMENTO SALARIAL')
sal = float(input('Salário atual:\nR$: '))
if sal > 1250.00:
    print('Seu salário, que era de R${:.2f}, passa a ser de R${:.2f}'.format(sal, sal*1.10))
    print('Aumento de 10%')
else:
    print('Seu salário, que era de R${:.2f}, passa a ser de R${:.2f}'.format(sal, sal*1.15))
    print('Aumento de 15%.')
