print('\033[1mGerador de Tabuadas\033[m\nEscreva qualquer número negativo para encerrar o programa')
while True:
    n = int(input('Digite um número: '))  # 1 - Perguntar de qual número o usuário quer ver a tabuada
    print('--'*10)
    if n < 0:  # logo de início, se o valor for negativo, o programa encerra SEM gerar a tabuada
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')  # gerar a tabuada (usarei a estrutura for)
    print('--'*10)
print('Programa encerrado.\nVolte sempre!')
