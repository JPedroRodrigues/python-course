from ex115.lib.interface import titulo, leiaint


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as e:
        print(f'\033[31mProblema ao criar arquivo: {e.__class__}\033[m')
    else:
        print(f'\033[32mArquivo \"{nome}\" criado com sucesso.\033[m')


def ler_arquivo(nome):
    if not arquivo_existe(nome):
        titulo('modelo de lista cadastral', 'roxo')
        print(f'{"Nome do indivíduo":<30}{"Idade em anos":>20}')
    else:
        with open(nome, 'rt') as file:
            titulo('lista de cadastrados', 'roxo')
            for line in file:
                dados = line.replace('\n', '').split(';')
                print(f'{dados[0]:<30}{dados[1]:>15} anos')


def cadastrar(nome, n='<desconhecido>', i=0):
    with open(nome, 'a') as file:
        file.write(f'{n};{i}\n')
