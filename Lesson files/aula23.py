try:
    n = int(input('Insira o numerador: '))
    d = int(input('Insira o denominador: '))
    r = n/d
except Exception as erro:
    print(f'\033[4;36mInfelizmente ocorreu um erro...\033[m\nDefinição: {erro.__class__}')
else:
    print(f'O resuldado da operação {n} / {d} é igual a {r:.2f}')
finally:
    print('Volte sempre!')

try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    c = a / b
except (TypeError, ValueError):
    print('Tipo de dado inserido é considerado inválido para o programa.')
except ZeroDivisionError:
    print('Nenhum número pode ser dividido por 0!')
except KeyboardInterrupt:
    print('Parece que o usuário não quis digitar nada...')
else:
    print(f'O resultado da divisão entre {a} e {b} é igual a {c:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
