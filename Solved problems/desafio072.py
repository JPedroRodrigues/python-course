contagem = 'zero', 'um', 'dois', 'três', 'quatro',\
           'cinco', 'seis', 'sete', 'oito', 'nove',\
           'dez', 'onze', 'doze', 'treze', 'quatorze',\
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Tente nomavente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {contagem[n]}')
    perg = int(input('Quer continuar? [1]Sim/[0]Não: '))
    while perg != 0 and perg != 1:
        perg = int(input('Opção inválida. Quer continuar? [1]Sim/[0]Não: '))
    if perg == 0:
        break
print('Programa encerrado. Tenha um bom dia!')
