from datetime import date
print('CHECAGEM - SERVIÇO MILITAR')
genero = str(input('Informe o seu gênero (masculino, feminino): ')).strip().upper()
if genero in 'MASCULINO MASC':
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    print('Completará {} anos neste ano.'.format(idade))
    if idade == 18:
        print('Você precisa se alistar neste ano ({}).\nProcure a base militar mais próxima.'.format(atual))
    elif idade < 18:
        margem = 18 - idade
        print('Você se alistará daqui a {} ano(s), em {}.'.format(margem, margem + atual))
    else:
        margem = idade - 18
        perg = str(input('Você já se alistou? Responda "sim ou não": ')).strip().upper()
        if perg == 'SIM':
            print('Para mais informações, acesse o site do exército brasileiro.')
        elif perg in 'NÃO NAO':
            print('Seu período de alistamento foi a {} ano(s) atrás, em {}.'.format(margem, atual - margem))
            print('Procure imediatamente a base militar mais próxima.')
        else:
            print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
elif genero in 'FEMININO FEM':
    print('Não há obrigatoriedade quanto ao seu alistamento.')
    print('Caso possua interesse, acesse o site do exército brasileiro ou procure a base militar mais próxima.')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
