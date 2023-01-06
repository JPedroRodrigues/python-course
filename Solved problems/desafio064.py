n = contador = soma = 0  # Quaisquer dessas variáveis recebe o mesmo valor 0.
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número: '))
    # O input abaixo do while impede que o programa realize um novo looping e calcule a soma do 999
    # Sim, isso é uma gambiarra
print('Você digitou {} números e a soma entre eles é igual a {}.'.format(contador, soma))
