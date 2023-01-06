def analise(*conjunto):
    from time import sleep
    contador = maior = 0
    print('='*40)
    print('Analisando o conjunto numérico...')
    sleep(1)
    for numero in conjunto:
        print(numero, end=' ')
        sleep(0.5)
        if contador == 0 or numero > maior:
            maior = numero
        contador += 1
    print(f'\nForam digitados, ao todo, {contador} números.')
    print(f'O maior número do conjunto é {maior}.')


# Programa principal
analise(2, 8, 6, 4, 7)
analise(9, 0)
analise(1)
analise()
