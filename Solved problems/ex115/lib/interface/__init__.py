cor = {
    'nada': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'roxo': '\033[35m',
    'azul': '\033[36m'
}


def line(size=50):
    """
    Cria uma linha de separação, utilizando '='.
    :param size: (Opcional) Número de caracteres da linha. Possui por padrão 50 caracteres.
    :return: Linha de separação personalizada.
    """
    return '=' * size


def titulo(txt='', clr='nada', size=50):
    """
    Mostra um título formatado, seguindo o padrão linha-título-linha.
    :param txt: Texto a ser inserido como título.
    :param size: Número de caracteres para a formatação do título e das linhas. Tem por padrão 50 caracteres.
    :param clr: Cores para personalizar o texto do título. Possui, como opções: vermelho, verde, amarelo, roxo e azul.
    Por padrão, não há cor de personalização.
    :return: Sem retorno.
    """
    print(line(size))
    print(cor[clr], end='')
    print(txt.upper().center(size), end='')
    print(cor['nada'])
    print(line(size))


def leiaint(prompt=''):
    """
    Função destinada à leitura de números inteiros.
    :param prompt: Mensagem a ser lida antes da captação do número.
    :return: Número inteiro.
    """
    while True:
        try:
            n = int(input(prompt))
        except (TypeError, ValueError):
            print(f'{cor["vermelho"]}{"ERRO! Digite um número inteiro válido"}{cor["nada"]}')
            continue
        except KeyboardInterrupt:
            print(f'\n{cor["amarelo"]}{"O usuário não inseriu um valor"}{cor["nada"]}')
            return 0
        else:
            return n


def menu(lista, clr1='nada', clr2='nada'):
    c = 1
    titulo('Menu de opções', clr1)
    for item in lista:
        print(f'{cor[clr1]}{c}{cor["nada"]} - {cor[clr2]}{item}{cor["nada"]}')
        c += 1
    print(line())
    n = leiaint(f'{cor[clr1]}Digite um número de acordo com a opção:{cor["nada"]} ')
    return n
