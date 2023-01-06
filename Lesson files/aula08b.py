from random import choice
escolha = str(input('Primeira Letra: '))
escolha2 = str(input('Segunda Letra: '))
escolha3 = str(input('Terceira Letra: '))
lista = [escolha, escolha2, escolha3]
print('A letra escolhida foi a letra {}.'.format(choice(lista)))
