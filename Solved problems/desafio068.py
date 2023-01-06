from random import randint
print('\033[1mVamos brincar de PAR ou ÍMPAR!\033[m')
contador = 0
while True:
    pc = randint(0, 10)
    print('--'*10)
    n = int(input('Digite o seu número: '))
    soma = n+pc
    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'
    option = str(input('Quer "PAR" ou "ÍMPAR"? ')).strip().capitalize()
    while option not in 'ParÍmpar':
        print('(Digite corretamente a sua opção)')
        option = str(input('Quer "PAR" ou "ÍMPAR"? ')).strip().capitalize()
    print('--'*10)
    if option == resultado:
        print('Você venceu!')
        print(f'{n} + {pc} = {soma} -> {resultado}')
        contador += 1
    else:
        print('Que pena, você perdeu...')
        print(f'Sua escolha: {option}')
        print(f'{n} + {pc} = {soma} -> {resultado}')
        break
print('--'*10)
print(f'N° de vitórias seguidas: {contador}')
