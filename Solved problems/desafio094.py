pessoa = {}
grupo = []
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Insira o seu nome: ')).strip().upper()
    pessoa['idade'] = int(input('Sua idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo: [M]/[F]: ')).strip().upper()
        if pessoa['sexo'] not in 'MF' or pessoa['sexo'] == '':
            print('Erro! Digite apenas M ou F')
        else:
            break
    grupo.append(pessoa.copy())
    while True:
        option = str(input('Cadastrar mais uma pessoa? (Sim/Não): ')).strip().lower()
        if option not in 'simnãonao' or option == '':
            print('Erro! Digite apenas "sim" ou "não".')
        else:
            break
    if option in 'nãonao':
        print(f'{"| Programa Encerrado |":=^50}')
        break
    print('='*50)
media = soma/len(grupo)
print(f'Nº de pessoas cadastradas: {len(grupo)}')
print(f'Média de idade do grupo: {media:.1f} anos')
print('Nome das mulheres cadastradas no grupo:')
for c in range(len(grupo)):
    if grupo[c]['sexo'] == 'F':
        print(f'- {grupo[c]["nome"]}')
print(f'Pessoas que estão acima da média de idade: ')
for c in range(len(grupo)):
    if grupo[c]['idade'] > media:
        for k, v in grupo[c].items():
            print(f'{k.title()} = {v};', end=' ')
        print()
