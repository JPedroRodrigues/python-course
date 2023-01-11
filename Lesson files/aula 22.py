print(f'{"| MODULARIZAÇÃO |":=^50}')
def fatorial(n, p=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if p:
            print(f'{c}', end=' x ' if c != 1 else f' = {f}')
    return f


number = int(input('Digite um número e eu lhe direi seu fatorial: '))
fat = fatorial(number, True)
print(f'\nO fatorial de {number} é {fat}')
print('A continuação desta aula se encontra na pasta "módulos"!')
