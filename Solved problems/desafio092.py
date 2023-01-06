from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
cadastro['idade'] = f'{datetime.now().year - ano} anos'
cadastro['CTPS'] = int(input('Nº da Carteira de Trabalho (digite 0 se não tiver): '))
if cadastro['CTPS'] > 0:
    cadastro['contratação'] = 0
    while cadastro['contratação'] <= ano+13:
        cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = f'{float(input("Salário atual: R$"))}'
    tempo = datetime.now().year - cadastro['contratação']
    if tempo < 35:
        apos = 35 - tempo
        cadastro['aposentadoria'] = f'Se aposenta com {cadastro["idade"] + apos} anos'
    else:
        cadastro['aposentadoria'] = 'Elegível para a aposentadoria.'
for k, v in cadastro.items():
    print(f'{k.capitalize()}: {v}')
