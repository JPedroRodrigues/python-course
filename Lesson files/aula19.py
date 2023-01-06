estado = {}
brasil = []
for c in range(3):
    estado['uf'] = str(input('Nome do Estado brasileiro: ')).title()
    estado['sigla'] = str(input('Sigla deste estado: ')).upper()
    brasil.append(estado.copy())
for dicionario in brasil:
    for values in dicionario.values():
        print(values, end=' ')
    print()
