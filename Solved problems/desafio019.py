from random import choice
a = str(input('Diga o nome de um aluno: '))
b = str(input('Diga o nome de outro aluno: '))
c = str(input('Do terceiro: '))
d = str(input('Do quarto: '))
lista = [a, b, c, d]
print('Dos quatro alunos, {} foi selecionado aleatoriamente.'.format(choice(lista)))
#A lista, em colchetes [], engloba as variáveis que eu criei e o comando choice seleciona um item desta lista
#poderia fazer assim: .format(choice([a, b, c, d]))
