from random import randint
print('Tente advinhar o número aleatório que o PC escolheu entre 0 e 10!')
pc = randint(0, 10)
acertou = False
contador = 0
while not acertou:
    jogador = int(input('Seu palpite: '))
    contador += 1
    if jogador == pc:
        acertou = True
    else:
        print('Errado!', end=' ')
        if jogador > pc:
            print('O número é menor que esse...')
        elif jogador < pc:
            print('O número é maior...')
print('Correto! O computador também pensou no número "{}".\nNº de tentativas: {}'.format(pc, contador))
