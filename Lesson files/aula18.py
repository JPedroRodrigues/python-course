galera = list()
dado = []
maior = 0
menor = 0
for c in range(5):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Existem {maior} pessoas maiores de idade e {menor} pessoas menores de idade.')
