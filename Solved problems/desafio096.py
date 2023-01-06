def area(a, b):
    medida = a*b
    print(f'O terreno, de medidas {a} x {b} m, possui uma área de {medida:.2f} m²')


# Programa principal
print(f'{"| ÁREA DE TERRENOS |":=^50}')
largura = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(b=largura, a=comp)
