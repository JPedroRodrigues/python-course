print('CÁLCULO DO ÍNDICE DE MASSA CORPORAL (IMC)')
nome = str(input('Olá, qual é o seu nome? ')).strip().title().split()
altura = float(input('Me informe a sua altura, em metros: '))
peso = float(input('Agora, por favor, me informe o seu peso, em kg: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    sit = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    sit = 'Peso ideal'
elif 25 <= imc < 30:
    sit = 'Sobrepeso'
elif 30 <= imc <= 40:
    sit = 'Obesidade'
else:
    sit = 'Obesidade mórbida'
print('{}, a sua situação pode ser definida como: {}'.format(nome[0], sit))
print('Seu índice: {:.1f}'.format(imc))
