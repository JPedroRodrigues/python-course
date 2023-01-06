cor = {'mirim': '\033[1;30m', 'infantil': '\033[1;32m', 'junior': '\033[1;33m',
       'senior': '\033[1;34m', 'master': '\033[1;35m', 'l': '\033[m', 'vermelho': '\033[1;31m'}
print('CHECAGEM DE CATEGORIAS')
idade = int(input('Informe a sua idade: '))
if 0 <= idade <= 9:
    categoria = '{}MIRIM{}'.format(cor['mirim'], cor['l'])
elif idade <= 14:
    categoria = '{}INFANTIL{}'.format(cor['infantil'], cor['l'])
elif idade <= 19:
    categoria = '{}JUNIOR{}'.format(cor['junior'], cor['l'])
elif idade <= 20:
    categoria = '{}SÊNIOR{}'.format(cor['senior'], cor['l'])
elif idade > 20:
    categoria = '{}MASTER{}'.format(cor['master'], cor['l'])
else:
    categoria = '{}Não há categorias para a idade informada{}'.format(cor['vermelho'], cor['l'])
print('A sua cateoria é: {}'.format(categoria))
