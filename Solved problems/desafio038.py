n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor, {}, é maior do que o segundo, {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor, {}, é maior do que o primeiro, {}.'.format(n2, n1))
else:
    print('Não existe valor maior, pois ambos são iguais.')
print('Tenha um bom dia!')
