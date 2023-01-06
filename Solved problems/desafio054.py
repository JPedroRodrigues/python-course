import datetime
print('\033[7;30;41mQuem é aqui é maior de idade?\033[m')
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('{}° - Ano de nascimento: '.format(c)))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('N° de pessoas maiores de idade: {}\nN° de pessoas menores de idade: {}'.format(maior, menor))
