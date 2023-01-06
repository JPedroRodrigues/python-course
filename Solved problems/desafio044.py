print('{:-^60}'.format(' \033[4;36mLOJAS JOÃO PEDRINHO\033[m '))
valor = float(input('Valor da compra: R$'))
print('''SELECIONE O MODO DE PAGAMENTO:
[1]: À vista - dinheiro/cheque
[2]: À vista - cartão
[3]: 2x no cartão
[4]: 3x ou mais no cartão''')
modo = int(input('Opção escolhida (digite somente números): '))
if modo == 1:
    print('Direito a 10% de desconto.')
    print('Valor: R${:.2f}'.format(valor * 0.90))
elif modo == 2:
    print('Direito a 5% de desconto.')
    print('Valor: R${:.2f}'.format(valor * 0.95))
elif modo == 3:
    print('2 parcelas de R${:.2f}, sem juros.'.format(valor / 2))
    print('Valor total: R${:.2f}'.format(valor))
elif modo == 4:
    par = int(input('N° de parcelas: '))
    print('Juros de 20%: {} parcelas de R${:.2f}'.format(par, (valor * 1.20) / par))
    print('Valor total: R${:.2f}'.format(valor * 1.20))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
