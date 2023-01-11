from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
# Programa principal
file = 'cadastro.txt'
if not arquivo_existe(file):
    criar_arquivo(file)
while True:
    opc = menu(['Lista de cadastrados', 'Cadastrar nova pessoa', 'Encerrar o programa'], 'verde', 'roxo')
    if opc == 1:  # Listagem de cadastrados
        ler_arquivo(file)
    elif opc == 2:  # Cadastro de uma nova pessoa
        titulo('Novo cadastro', 'roxo')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrar(file, nome, idade)
    elif opc == 3:  # Encerramento do programa
        titulo('Programa encerrado', 'vermelho')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
