ficha = dict()
ficha['nome'] = str(input('Nome do aluno: ')).strip().title()
ficha['média'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['média'] >= 6:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['média'] < 6:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
print('='*30)
for keys, values in ficha.items():
    print(f'{keys.capitalize()}: {values}')
