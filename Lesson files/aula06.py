print('Olá, seja bem-vindo ao nosso teste!')
nome = input('Qual é o seu nome? ')
print('Que bom ter você por aqui, {}!'.format(nome))
print('Vamos começar!')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
# print('A soma entre', n1, 'e', n2, 'é: {}!'.format(soma))
print('A soma entre {} e {} é {}!'.format(n1, n2, soma))
print('Agora vamos conferir se este computador funciona: ')
question = input('Digite qualquer coisa: ')
answer = question.isnumeric()
print('Isto que você digitou, "{}", é um número? Resposta: {}'.format(question, answer))
