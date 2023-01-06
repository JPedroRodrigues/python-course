import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação destes alunos será: {}.'.format(lista))

from random import shuffle
alunos = 'Sérgio Otávio Marcos Luis'.split()
shuffle(alunos)
print('Ordem de apresentação: {}.'.format(alunos))
