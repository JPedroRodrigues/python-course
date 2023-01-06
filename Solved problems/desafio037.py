
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] para BINÁRIO')
print('[2] para OCTAL')
print('[3] para HEXADECIMAL')
r = int(input('Digite o número da opção: '))
if r == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(n, bin(n)[2:]))
elif r == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(n, oct(n)[2:]))
elif r == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE\033[m')
