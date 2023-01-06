def contador(start, end, step):
    from time import sleep
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print('-'*50)
    print(f'Contagem de {start} até {end}, de {step} em {step}.')
    sleep(2.5)
    if start <= end:
        while start <= end:
            print(f'{start}', end=' ', flush=True)
            sleep(0.5)
            start += step
        print()
    elif start >= end:
        while start >= end:
            print(f'{start}', end=' ', flush=True)
            sleep(0.5)
            start -= step
        print()


# Programa principal
contador(1, 10, -1)
contador(10, 0, 0)
print('-'*50)
print('Agora é a sua vez! Escreva os números pedidos para gerar a sequência.')
inicio = int(input('Número inicial: '))
final = int(input('Número final: '))
passo = int(input('De quanto em quanto? Passo: '))
contador(inicio, final, passo)
