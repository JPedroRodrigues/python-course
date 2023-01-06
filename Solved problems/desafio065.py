r = ''
soma = maior = menor = contador = 0
while r in 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = str(input('Quer continuar?[S]/[N]: ')).strip().upper()[0]
    if r not in 'SN':
        print('Resposta inválida. Tente novamente.')
        r = str(input('Quer continuar?[S]/[N]: ')).strip().upper()[0]
media = soma/contador
print('A média dos {} valores digitados é igual a {:.2f}.'.format(contador, media))
print('Maior valor: {}\nMenor valor: {}'.format(maior, menor))
