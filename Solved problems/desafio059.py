from time import sleep
print('''MENU DE OPÇÕES MATEMÁTICAS
[1] Somar
[2] Multiplicar
[3] Maior
[4] Reescrever os números
[5] Sair do programa
''')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo valor: '))
r = int
while r != 5:
    print('--'*10)
    r = int(input('Sua opção: '))
    if r == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif r == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif r == 3:
        if n1 > n2:
            print('Maior valor: {}'.format(n1))
        elif n2 > n1:
            print('Maior valor: {}'.format(n2))
        else:
            print('Ambos são iguais!')
    elif r == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Outro número: '))
    elif r == 5:
        print('Finalizando', end='')
        for c in range(3):
            sleep(0.5)
            print('.', end='')
    else:
        print('Opção inválida. Digite a opção corretamente.')
sleep(0.5)
print('Foi um prazer tê-lo por aqui. Um bom dia!')
