sxo = str(input('Informe o seu sexo[M/F]: ')).strip().upper()[0]
while sxo not in 'MF':
    sxo = str(input('\033[1;33mOpção iválida. Responda o item corretamente:\n[M/F]: \033[m')).strip().upper()[0]
if sxo == 'M':
    sxo = '\033[1;34mMasculino\033[m'
elif sxo == 'F':
    sxo = '\033[1;31mFeminino\033[m'
print('Tenha um bom dia! A sua resposta foi: {}'.format(sxo))
