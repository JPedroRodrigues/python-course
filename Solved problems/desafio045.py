from random import randint
from time import sleep
cor = {'roxo': '\033[1;35m', 'l': '\033[m', 'azul': '\033[1;34m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m'}
cor2 = {'branco': '\033[1;30m', 'vermelho': '\033[1;31m'}
print('{:-^40}'.format('\033[1;31mJOKENPÔ!!\033[m'))
print('Desafie a máquina em um duelo!')
itens = ('{}Pedra{}'.format(cor['azul'], cor['l']),
         '{}Papel{}'.format(cor['verde'], cor['l']),
         '{}Tesoura{}'.format(cor['roxo'], cor['l']))
pc = randint(0, 2)
print('''Escolha uma opção:
[{}0{}] Pedra
[{}1{}] Papel
[{}2{}] Tesoura
[3] Regras'''.format(cor['azul'], cor['l'], cor['verde'], cor['l'], cor['roxo'], cor['l']))
ply = int(input('Sua escolha: '))
if ply == 0 or ply == 1 or ply == 2:
    print('{}JO'.format(cor2['vermelho']))
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ{}'.format(cor['l']))
    sleep(0.5)
if ply == 0 and pc == 2 or ply == 1 and pc == 0 or ply == 2 and pc == 1:
    print('{}VOCÊ VENCEU! PARABÉNS!{}'.format(cor['verde'], cor['l']))
    print('Escolha da máquina: {}\nSua jogada: {}'.format(itens[pc], itens[ply]))
elif ply == pc:
    print('{}EMPATE!{}'.format(cor['amarelo'], cor['l']))
    print('Escolha da máquina: {}\nSua jogada: {}'.format(itens[pc], itens[ply]))
elif ply == 0 and pc == 1 or ply == 1 and pc == 2 or ply == 2 and pc == 0:
    print('\033[1;31mDERROTA...{}'.format(cor['l']))
    print('Mas não se decepcione, tente outra vez!')
    print('Escolha da máquina: {}\nSua jogada: {}'.format(itens[pc], itens[ply]))
elif ply == 3:
    print('''{}REGRAS{}
{} ganha de {}
{} ganha de {}
{} ganha de {}'''.format(cor2['vermelho'], cor['l'], itens[0], itens[2], itens[2], itens[1], itens[1], itens[0], ))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA.\nESCOLHA CORRETAMENTE  AS ALTERNATIVAS\033[m')
