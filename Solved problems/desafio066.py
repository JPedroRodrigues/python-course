print('Operações numéricas.\n(Digite 999 para encerrar o programa)')
contador = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Muito bem!\nForam digitados {contador} números e a soma entre eles é igual a {soma}.')
