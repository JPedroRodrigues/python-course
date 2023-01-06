c = ('\033[m',      # Sem cor
     '\033[7;31m',  # Fundo vermelho
     '\033[7;32m',  # Fundo verde
     '\033[7;35m',  # Fundo roxo
     '\033[7;36m',  # Fundo azul claro
     )


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('-'*(len(msg)+4))
    print(f'  {msg}')
    print('-'*(len(msg)+4))
    print(c[0], end='')


def ajuda(comando):
    titulo(f'Procurando dados sobre \'{q}\'...', 3)
    print(c[4], end='')
    help(comando)
    print(c[0], end='')


while True:
    titulo('Sistema de ajuda PyHelp', 2)
    print('Digite "fim" para encerrar o programa.')
    q = str(input('Digite o nome de uma função ou biblioteca: ')).strip()
    if q in 'fim':
        titulo('Programa encerrado', 1)
        break
    else:
        ajuda(q)
