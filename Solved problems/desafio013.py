print('Bom dia, confira aqui o aumento dado em seu salário')
s = float(input('Digite aqui o valor de sua remuneração: R$'))
acrescimo = s*(15/100)
a = s*1.15
print('Seu novo salário, com um aumento de {:.2f}% (R${:.2f}), vale {:.2f}!'.format(((a/s)-1)*100, acrescimo, a))
