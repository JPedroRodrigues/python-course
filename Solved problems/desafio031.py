print('CUSTO DE VIAGEM')
d = float(input('Digite a distância percorrida em sua viagem. Km: '))
if d <= 200.0:
    preco = d * 0.50
    print('Curta distância')
    print('O preço a ser pago é de R${:.2f}'.format(preco))
else:
    preco = d * 0.45
    print('Longa distância')
    print('Será cobrado R${:.2f} pela sua viagem.'.format(preco))

# Posso fazer da seguinte forma:
# if d <=200:
#   preço = d * 0.50
# else:
#   preço = d * 0.45
# print ('O preço é de R${:.2f}'.format(preço))
# DA forma simplificada:
# preço = distancia * 0.50 if d <= 200 else distancia 0.45
