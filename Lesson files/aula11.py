import time
nome = str(input('\033[1;33;45mMe diga seu nome completo:\033[m ')).strip()
print('\033[7;30;41mProcessando...\033[m')
time.sleep(1)
per = str(input('\033[1;33;44mSeu nome possui {} letras? Responda "sim" ou não": '.format(len(nome) - nome.count(' ')))).title()
if per == 'Sim':
    print('\033[1;35mUau! Parece que este computador sabe contar.')
else:
    print('\033[1;36mBom, todo mundo erra... né?\033[m')
#É POSSÍVEL FAZER DESTA FORMA!!!
apelido = str(input('Nickname: ')).strip()
cores = {'vermelhonegrito':'\033[4;31m', 'limpa':'\033[m'}
print('Bem vindo ao jogo, {}{}{}!'.format(cores['vermelhonegrito'], apelido, cores['limpa']))
