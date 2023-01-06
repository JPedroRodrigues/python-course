from random import randint
from time import sleep
print('---'*29)
print('O computador selecionou um número inteiro entre 0 e 5. Consegue pensar em qual seria?')
print('---'*29)
n = int(input('Desafio-te a advinhar este número: '))
print('Processando...')
sleep(2)
r = randint(0, 5)
if n == r:
    print('Parabéns, você venceu o desafio!')
else:
    print('Não foi desta vez... o número era {}!'.format(r))
