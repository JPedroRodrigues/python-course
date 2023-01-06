above18 = men = wunder20 = 0
while True:
    idade = int(input('Insira a sua idade: '))
    if idade > 18:
        above18 += 1
    sxo = ' '  # Precisa ficar separado
    while sxo not in 'MF':
        sxo = str(input('Informe o sexo: [M]/[F] ')).strip().upper()[0]
    if sxo == 'M':
        men += 1
    if sxo == 'F' and idade < 20:
        wunder20 += 1
    perg = int
    while perg not in (0, 1):
        perg = int(input('Quer continuar? [1]Sim/[0]Não '))
    if perg == 0:
        break
print(f'N° de pessoas com mais de 18 anos: {above18}')
print(f'Nº de homens cadastrados: {men}')
print(f'Nº de mulheres abaixo dos 20 anos: {wunder20}')
