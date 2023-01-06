from time import sleep
cor = {'azulclaro': '\033[36m', 'amarelo': '\033[1;33m',
       'limpa': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}
print('\033[36m-\033[m'*23)
print('{}AVALIAÇÃO DE EMPRÉSTIMO{}'.format(cor['amarelo'], cor['limpa']))
print('\033[36m-\033[m'*23)
print('{}COMPRA DE IMÓVEL:{}'.format(cor['amarelo'], cor['limpa']))
nome = str(input('Por favor, insira o seu nome: ')).title().strip().split()
valor = float(input('Valor do imóvel: {}R${} '.format(cor['verde'], cor['limpa'])))
sal = float(input('Salário do requerinte: {}R$:{} '.format(cor['verde'], cor['limpa'])))
anos = float(input('Tempo de pagamento, em anos: '))
prest = valor / (anos*12)
limite = sal * 0.30
print('{}ANALISANDO...{}'.format(cor['amarelo'], cor['limpa']))
sleep(1)
if prest > limite:
    print('{}Empréstimo Negado{}'.format(cor['vermelho'], cor['limpa']))
    print('{}O valor da prestação (R${:.2f}) excedeu o'
          ' valor equivalente a 30% do seu salário.{}'.format(cor['vermelho'], prest, cor['limpa']))
elif prest < limite:
    print('{}Parabéns, seu empréstimo foi aprovado!{}'.format(cor['verde'], cor['limpa']))
    print('{}Valor das prestações: R${:.2f}{}'.format(cor['verde'], prest, cor['limpa']))
elif prest == limite:
    print('{}Parabéns, seu empréstimo foi aprovado!{}'.format(cor['verde'], cor['limpa']))
    print('{}Porém, atente-se, pois o valor da prestação '
          'está na margem limite do seu salário: R${:.2f}{}'.format(cor['vermelho'], prest, cor['limpa']))
print('{}É um prazer recebê-lo em nossa agência, {}.'
      ' Tenha um bom dia!{}'.format(cor['amarelo'], nome[0], cor['limpa']))
