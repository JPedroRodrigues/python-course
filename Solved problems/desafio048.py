s = 0  # se chama acumulador
cont = 0  # se chama contador
for c in range(3, 501, 6):
    s += c  # s = s + c --> "s" recebe o valor de "s" mais os valores de "c"
    cont = cont + 1  #Nosso contador adiciona sempre +1
print('O valor da soma dos {} números ímpares divisíveis por 3 e que estão entre 1 e 500 é igual a {}'.format(cont, s))
