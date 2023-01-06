def leiaint(prompt=''):
    """
    Função capaz de realizar uma leitura de um número inteiro.
    :param prompt: Saída de texto para a recepção de um número.
    :return: Número inteiro digitado.
    """
    cor = {'vermelho': '\033[1;31m', 'none': '\033[m'}
    validation = False
    while True:
        n = str(input(prompt))
        if n.isnumeric():
            n = int(n)
            validation = True
        else:
            print(f'{cor["vermelho"]}Erro. A função leiaint() aceita somente números inteiros.{cor["none"]}')
        if validation:
            break
    return n


# Programa principal
numero = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')
print(f'Vejamos sua raíz quadrada: {numero}² = {pow(numero, 2)}')
