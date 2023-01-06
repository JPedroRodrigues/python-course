n = int(input('Qual é o número de pessoas que serão analisadas? '))
idade_total = 0
maior_idade_h = 0
homem_mais_velho = ''
contador = 0
for c in range(1, n+1):
    print('=== {}º PESSOA ==='.format(c))
    nome = str(input('Seu nome: ')).strip().upper()
    idade = int(input('Sua idade: '))
    sxo = str(input('Sexo [M/F]: ')).strip().upper()
    idade_total += idade
    if c == 1 and sxo in 'M':
        maior_idade_h = idade
        homem_mais_velho = nome
    if sxo in 'M' and idade > maior_idade_h:
        maior_idade_h = idade
        homem_mais_velho = nome
    if sxo in 'F' and idade < 20:
        contador += 1
media = idade_total/n
print('A média de idade do grupo é: {}'.format(media))
print('{}, com {} anos, é o homem mais velho.'.format(homem_mais_velho, maior_idade_h))
print('Número de mulheres abaixo de 20 anos: {}'.format(contador))
