print('Parabéns, você acabou de ganhar 5% de desconto na compra de qualquer produto!')
o = str(input('Qual produto você pretende comprar? '))
p = float(input('E qual é o seu preço? '))
print('{}, com o desconto, fica por {:.2f} reais.'.format(o, p*0.95))
