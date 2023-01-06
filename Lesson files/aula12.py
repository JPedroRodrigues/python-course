resp = str(input('Olá, podemos confirmar nossa consulta? Resposta: ')).upper().strip()
if resp == 'SIM' or resp == 'SIM!':
    print('Certo! Lembre-se de chegar 30 minutos antes do combinado.')
elif resp == 'NÃO SEI' or resp == 'SEI LÁ' or resp == 'TALVEZ':
    print('Então se decida!')
elif resp in 'SIKM sim nao oism sima naom NAO':
    print('O que?!')
else:
    from time import sleep
    sleep(1)
    print('...')
    sleep(1)
print('Tenha um bom dia!')
