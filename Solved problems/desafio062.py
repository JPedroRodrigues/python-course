print('\033[1;36m--\033[m'*20)
print('\033[1;31mGERADOR DE PROGRESSÕES ARITMÉTICAS(PA)\033[m')
print('\033[1;36m--\033[m'*20)
print('Vamos começar com os 10 primeiros termos.')
primeiro = int(input('\033[1;31m1\033[m - Insira o primeiro termo: '))
r = int(input('\033[1;31m2\033[m - Digite a razão desta PA: '))
a1 = primeiro
contador = 1
total = 0
adicional = 10
while adicional != 0:
    total = total + adicional
    print('\033[1;31mProgressão\033[m: ', end='')
    while contador <= total:
        print('{}'.format(a1), end=' ')
        a1 += r
        contador += 1
    adicional = int(input('\nQuer quantos termos a mais? '))
print('Pronto!\nAo todo, {} termos foram gerados.'.format(total))
