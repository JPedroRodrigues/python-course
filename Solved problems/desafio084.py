grupo = []
dados = list()
peso = []
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: Kg')))
    grupo.append(dados[:])
    dados.clear()
    r = ' '
    while r not in '01' or r == '':
        r = str(input('[1]Adicionar/[0]Encerrar: ')).strip()
    if r in '0':
        print('--'*20)
        break
print(f'Nº de pessoas cadastradas: {len(grupo)}')
for kg in grupo:
    peso.append(kg[1])
print(f'Nome da(s) pessoa(s) mais pesada(s)({max(peso):.2f}Kg): ', end='')
for p in grupo:
    if p[1] == max(peso):
        print(p[0], end='.. ')
print(f'\nNome da(s) pessoa(s) mais leve(s)({min(peso):.2f}Kg): ', end='')
for p in grupo:
    if p[1] == min(peso):
        print(p[0], end='.. ')
