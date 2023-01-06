soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
# print('A soma dos valores digitados é: {}'.format(soma))
print(f'A soma vale: {soma}')  # Um novo PEP (Python Enhancement Proposal) propôs este modo de formatação
# Preciso ver como me atualizar de acordo com esses PEP's
