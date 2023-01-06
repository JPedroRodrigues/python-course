from time import sleep
boletim = []
while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    n1 = n2 = -1
    while n1 > 10 or n1 < 0:
        n1 = float(input('1ª nota: '))
    while n2 > 10 or n2 < 0:
        n2 = float(input('2ª nota: '))
    media = (n1+n2)/2
    boletim.append([nome, [n1, n2], media])
    menu = ' '
    while menu not in 'SIMNÃONAO' or menu == '':
        menu = str(input('Adicionar mais alunos? [S]Sim/[N]Não: ')).strip().upper()
    if menu in 'NÃONAO':
        print(f'{"| Programa encerrado |":=^50}')
        break
print(f'{"Grando boletim"}', end='')
for c in range(3):
    sleep(0.7)
    print('.', end='')
print(f'\n{"| BOLETIM TRIMESTRAL |":=^50}')
print(f'\n{"Nº":<10}{"NOME":<30}{"MÉDIA":>10}')
for n, info in enumerate(boletim):
    print(f'{n:<10}{info[0]:<30}{info[2]:>10.2f}')
print('='*50)
while True:
    aluno = -1
    print(f'Digite "999" para encerrar o programa.')
    while aluno not in range(0, len(boletim)) and aluno != 999:
        aluno = int(input('Digite o número do aluno para ver suas notas: '))
    if aluno == 999:
        print(f'Programa encerrado.')
        break
    print(f'Notas do aluno {boletim[aluno][0]}: {boletim[aluno][1]}')
    print('='*50)
print(f'{"| VOLTE SEMPRE! |":=^50}')
