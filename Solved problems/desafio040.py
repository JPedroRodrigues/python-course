cor = {'vermelho': '\033[1;31m', 'amarelo': '\033[1;33m', 'verde': '\033[1;32m', 'limpa': '\033[m'}
print('\033[7;30mCHECAGEM DE MÉDIAS\033[m')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if 0 <= media <= 5.0:
    print('{}REPROVADO!{}'.format(cor['vermelho'], cor['limpa']))
elif 5 < media <= 6.9:
    print('{}RECUPERAÇÃO{}'.format(cor['amarelo'], cor['limpa']))
    print('Aguarde a disponibilização do cronograma para mais detalhes.')
elif 7 <= media <= 10:
    print('{}APROVADO{}'.format(cor['verde'], cor['limpa']))
else:
    print('\033[1;31mRESULTADO INVÁLIDO\033[m')
print('Sua média: {:.2f}'.format(media))
