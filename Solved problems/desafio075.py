n1 = (int(input('Digite um número: ')))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o último número: '))
tupla = n1, n2, n3, n4
ci = 0
number9 = tupla.count(9)
print(f'Nº de vezes em que o número 9 aparece: {tupla.count(9)}')
if 3 not in tupla:
    print('O número 3 não foi digitado nenhuma vez.')
else:
    print(f'O número 3 foi digitado, pela primeira vez, na {tupla.index(3)+1}ª posição')
print('Números pares digitados: ', end='')
if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
    print('não foram digitados números pares.')
else:
    for par in tupla:
        if par % 2 == 0:
            print(par, end=' ')
