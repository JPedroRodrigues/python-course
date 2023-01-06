import datetime
print('Identificador de ano bissexto')
ano = int(input('Digite um ano para saber se ele é bissexto ou não. Digite 0 para saber sobre o ano atual.\nAno: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
