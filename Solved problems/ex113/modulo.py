def leiaint(prompt=''):
    """
    -> Realiza a leitura de um número inteiro.
    :param prompt: Mensagem de saída da função que surge antes da recepção de um número inteiro.
    :return: Número inteiro.
    """
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print('\033[31mErro! Só serão aceitos números inteiros.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mPrograma encerrado abruptamente.\033[m')
            return 0
        else:
            return n


def leiareal(prompt=''):
    """
    -> Realiza a leitura de quaisquer números reais.
    :param prompt: Mensagem de saída da função que surge antes da recepção de um número real.
    :return: Número real.
    """
    while True:
        try:
            n = str(input(prompt)).strip().replace(',', '.')
            n = float(n)
        except (ValueError, TypeError):
            print('\033[31mSó serão aceitos números reais.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mPrograma encerrado abruptamente.\033[m')
            return 0
        else:
            return n
